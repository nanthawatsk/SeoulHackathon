from ultralytics import YOLO
import cv2
import os
from accident_analyzer import AccidentAnalyzer

def StartApplication(input_vid_path, output_vid_path, weight_path="weights/best.pt"):
    output_vid_path="output_video-1.mp4"
    model = YOLO(weight_path)

    image_save_folder = "accident_frame"
    os.makedirs(image_save_folder, exist_ok=True)
    frame_count = 0
    output_frame_count = 0


    video_path = cv2.VideoCapture(input_vid_path)

    fps = int(video_path.get(cv2.CAP_PROP_FPS))
    width = int(video_path.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_path.get(cv2.CAP_PROP_FRAME_HEIGHT))


    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_vid_path, fourcc, fps, (width, height))

    analyzer = AccidentAnalyzer()

    while True:
        ret, frame = video_path.read()

        if not ret:
            break
        
        results = model.predict(source=frame, show=False, save=False, save_txt=False)
        id = results[0].probs.top1
        clsName = results[0].names[id]
        if (results[0].probs.top1conf.cpu() >= 0.7) and (clsName != "Non Accident"):
            image_filename = f"{image_save_folder}/accident_img.jpg"
            if output_frame_count == 0:
                cv2.imwrite(image_filename, frame)
                image_path = "accident_frame/accident_img.jpg"
                output_text = analyzer.analyze_accident(image_path)
                output_frame_count += 1 
                
            
            color = (0,0,255)
            font_scale = width / 600  
            font_thickness = max(1, int(font_scale))  
            font = cv2.FONT_HERSHEY_COMPLEX
            textSize = cv2.getTextSize(clsName, font, font_scale, font_thickness)[0]
            textX = width - textSize[0] - 20 
            textY = textSize[1] + 20  
            cv2.putText(frame, clsName, (textX, textY), font, font_scale, color, font_thickness, cv2.LINE_AA)
            
        
        frame_count += 1 
        # Frame addjust when we use in real life because The same place got notification a lot it not impossible
        if frame_count >= 2000:
            output_frame_count = 0
        out.write(frame)
        
    out.release()   
    return output_text