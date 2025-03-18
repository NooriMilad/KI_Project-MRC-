def save_image(image, filename):
    import cv2
    cv2.imwrite(filename, image)

def log_illegal_plate(plate):
    import pandas as pd
    from datetime import datetime

    log_entry = {'Plate': plate, 'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    log_df = pd.DataFrame([log_entry])
    
    try:
        log_df.to_csv('src/data/illegal_log.csv', mode='a', header=False, index=False)
    except FileNotFoundError:
        log_df.to_csv('src/data/illegal_log.csv', index=False)