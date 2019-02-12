import pytube
import json

if __name__ == '__main__':

    kSquatsFile = open("/Users/parthvyas/Documents/SJSU/cs298/dataScraper/kinetics_train/kinetics_train.json")
    json_data = json.load(kSquatsFile)
    videoCounter = 0

    for val in json_data.values():
        if val["annotations"]["label"] == "squat":
            videoCounter+=1
            try:
                pytube.YouTube(val["url"]).streams.first().download('/Users/parthvyas/Documents/SJSU/cs298/datasets/kineticsActionVideoDataset/squatVideos400')
            except pytube.exceptions.VideoUnavailable:
                print("video unavailable")
                print(val["url"])
                print(videoCounter)
            except Exception:
                print("Some Error")
                print(videoCounter)

    print(videoCounter)