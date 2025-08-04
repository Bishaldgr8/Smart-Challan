# Tutorials/01_image_to_word/inferenceModel.py
if __name__ == "__main__":
    import pandas as pd
    from tqdm import tqdm
    from mltu.configs import BaseModelConfigs
    
    configs = BaseModelConfigs.load("Models/1_image_to_word/202211270035/configs.yaml")

    model = ImageToWordModel(model_path=configs.model_path, char_list=configs.vocab)

    df = pd.read_csv("Models/1_image_to_word/202211270035/val.csv").dropna().values.tolist()

    accum_cer = []
    for image_path, label in tqdm(df):
        image = cv2.imread(image_path)

        try:
            prediction_text = model.predict(image)

            cer = get_cer(prediction_text, label)
            print(f"Image: {image_path}, Label: {label}, Prediction: {prediction_text}, CER: {cer}")

            # resize image by 3 times for visualization
            # image = cv2.resize(image, (image.shape[1] * 3, image.shape[0] * 3))
            # cv2.imshow(prediction_text, image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
        except:
            continue
        
        accum_cer.append(cer)

    print(f"Average CER: {np.average(accum_cer)}")