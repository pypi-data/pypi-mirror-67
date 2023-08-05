import akida
import numpy as np
import copy


def _get_weights_params_identity(layer):
    """
    Creates an 'identity' convolutional layer parameters and its weights.
    """
    out_dims = layer.output_dims
    nb_chan = out_dims[2]
    weights = np.identity(nb_chan,
                          dtype=np.int8).reshape(1, 1, nb_chan, nb_chan)

    # create a layer to have default parameters
    identity_layer = akida.Convolutional(f"{layer.name}_pooling",
                                         1,
                                         1,
                                         nb_chan,
                                         threshold_fire=0,
                                         threshold_fire_bits=layer.parameters.
                                         activations_params.threshold_fire_bits,
                                         threshold_fire_step=1)
    return copy.copy(identity_layer.parameters), weights


def _copy_layer_variables(layer, copied_layer):
    for var in copied_layer.get_variable_names():
        layer.set_variable(var, copied_layer.get_variable(var))


def _copy_layer(model, layer):
    new_layer = akida.Layer(layer.parameters, layer.name)
    model.add(new_layer)
    _copy_layer_variables(new_layer, layer)


def _add_identity_cnp_after_max_pooling(model, layer):
    """
    Adds the layer and an identity CNP to the model
    """
    ident_params, ident_weights = _get_weights_params_identity(layer)
    identity_layer = akida.Layer(ident_params, f"{layer.name}_identity")
    model.add(identity_layer)
    identity_layer.set_variable("weights", ident_weights)


def _cnp_max_pooling(layer):
    return layer.parameters.layer_type in [
        akida.LayerType.Convolutional, akida.LayerType.SeparableConvolutional
    ] and layer.parameters.pooling_type == akida.PoolingType.Max


def _cnp_pooling_needs_identity_cnp(model, layer_index):
    """
    Returns True if the layer is CNP with max pooling not followed by another
    CNP, and we can add an identity CNP layer after it without altering result
    """
    result = False
    layer = model.get_layer(layer_index)
    if _cnp_max_pooling(layer):
        # if it is not the last layer, check the layer is not followed by another cnp
        if layer_index != model.get_layer_count() - 1:
            next_layer = model.get_layer(layer_index + 1)
            if next_layer.parameters.layer_type not in [
                    akida.LayerType.Convolutional,
                    akida.LayerType.SeparableConvolutional
            ]:
                result = True
        # if it is the last layer, we can add an identity layer only if it has activations enabled
        elif layer.parameters.activations_params.activations_enabled:
            result = True
    return result


def convert(model):
    """Tries to convert a model to an HW compatible one

    Tries to convert a model to an HW compatible one, using SW workarounds
    for known limitations. It returns a converted model that is not guaranteed
    to be HW compatible, depending if workaround have been found.

    Args:
        model (:obj:`Model`): a Model object to convert

    Returns:
        :obj:`Model`: a new converted Model with no guarantee that
        it is HW compatible.
    """
    new_model = akida.Model(backend=model.backend.type)
    nb_layers = model.get_layer_count()
    for i in range(nb_layers):
        layer = model.get_layer(i)
        # If CNP has max pooling and is not followed by another CNP, we can add
        # an identity CNP layer
        if _cnp_max_pooling(layer) and _cnp_pooling_needs_identity_cnp(
                model, i):
            _copy_layer(new_model, layer)
            _add_identity_cnp_after_max_pooling(new_model, layer)
            continue

        # if no particular case is found, copy the layer into the new model
        _copy_layer(new_model, layer)

    return new_model
