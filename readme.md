# Sea2Future

Sea2Future é um addon desenvolvido para o Blender

<br/>

## Ficheiro "\_\_init\_\_"

Funciona como Main Panel onde se agregam os sub-panels para cada funcionalidade deste addon, inicializando assim os mesmos.

<br/>

## Panels

- ### [Live Visualization Panel](./panels/live_visualization_panel.py)

  Panel correspondente à funcionalidade de visualização em tempo real da atitude da embarcação. Em função do tipo conecção selecionado serão apresentados diferentes parâmetros para essa ligação.

  - Socket
    - Endereço IP
    - Porto

<br/>

- ### [Load File Panel](./panels/generate_animation_panel.py)

  Panel correspondente à funcionalidade da criação de uma animação com base num ficheiro com dados sobre a posição, rotação ou ambos. Neste panel é possível selecionar o tipo de atitude que se pretende importar do ficheiro e aplicar ao objeto:

  - Position
  - Rotation
  - Both

  De seguida apenas é necessário selecionar o ficheiro de dados, e gerar a animação.

<br/>

## Operators

- ### [Live Visualization Operator](./operators/live_visualization_operator.py)

  Operator que permite visualizar em tempo real a atitude do barco. Apenas têm de receber essa informação a partir de uma fonte em tempo real, Ex: socket.

<br/>

- ### [Load File Operator](./operators/generate_animation_operator.py)

  Operator que permite a criação de uma animação utilizando um ficheiro com informação da posição, rotação ou ambos de um objecto.

<br/>

# TODO

- Verificar tipo de ficheiro csv
