total_electrons = int(input())

electron_config = []
current_layer = 1

while total_electrons > 0:
    current_layer_electrons = 2 * pow(current_layer, 2)

    if total_electrons >= current_layer_electrons:
        electron_config.append(current_layer_electrons)
    else:
        electron_config.append(total_electrons)

    total_electrons -= current_layer_electrons
    current_layer += 1

electron_config_str = [str(layer) for layer in electron_config]
print(f"[{', '.join(electron_config_str)}]")