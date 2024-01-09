from ultralytics import YOLO

model = YOLO('yolov8n-pose.pt') 

def main():
    results = model.train(data='data.yaml', epochs=50, imgsz=640, batch = 4, optimizer = 'SGD')

if __name__ == '__main__':
    main()