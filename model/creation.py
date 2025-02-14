from ultralytics import YOLO
from os.path import abspath, join, dirname
from os import pardir, system
import yaml
import torch
import torchvision

# Define la arquitectura del modelo YOLO
class YOLO(torch.nn.Module):
    def __init__(self, backbone, num_classes, grid_size, boxes_per_cell):
        super(YOLO, self).__init__()

        # Carga la red troncal preentrenada
        if backbone == "resnet50":
            self.backbone = torchvision.models.resnet50(pretrained=True)
            # Modifica la capa final para que coincida con el número de clases
            num_ftrs = self.backbone.fc.in_features
            self.backbone.fc = torch.nn.Linear(num_ftrs, grid_size[0] * grid_size[1] * (5 * boxes_per_cell + num_classes))
        else:
            raise ValueError(f"Backbone no soportado: {backbone}")

        self.grid_size = grid_size
        self.boxes_per_cell = boxes_per_cell
        self.num_classes = num_classes

    def forward(self, x):
        x = self.backbone(x)
        # Reorganiza la salida para que coincida con la forma de YOLO
        x = x.view(-1, self.grid_size[0], self.grid_size[1], 5 * self.boxes_per_cell + self.num_classes)
        return x


def main():
    file_path = abspath(__file__)
    file_dir = dirname(file_path)
    parent_dir = abspath(join(file_dir, pardir))
    datasets_dir = join(parent_dir, "datasets")
    yaml_file = join(datasets_dir, "dataset.yaml")

    # Carga el archivo YAML
    with open(yaml_file, "r") as f:
        config = yaml.safe_load(f)

    # Accede a los parámetros de configuración

    input_size = config["architecture"]["input_size"]
    backbone = config["architecture"]["backbone"]
    num_classes = config["architecture"]["num_classes"]
    grid_size = config["yolov11"]["grid_size"]
    boxes_per_cell = config["yolov11"]["boxes_per_cell"]


if __name__ == "__main__":
    system("cls")
    main()
