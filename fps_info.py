# -*- coding: utf-8 -*-

import os
import sys
import glob
import cv2

def read_video(video_path):
    video_read_capture = cv2.VideoCapture(video_path)

    fps = int(video_read_capture.get(cv2.CAP_PROP_FPS))
    num_frames = video_read_capture.get(cv2.CAP_PROP_FRAME_COUNT)

    video_read_capture.release()

    return num_frames, fps

def read_all_video(dataset_video_dir):
    if not os.path.exists(dataset_video_dir):
        print(f'dataset video dir {dataset_video_dir} is not exist!')
        sys.exit(0)

    # 获取视频目录下所有的子文件夹的路径名
    sentence_video_dir_list = glob.glob(f'{dataset_video_dir}/*')


    for video_dir_idx, single_sentence_video_dir in enumerate(sentence_video_dir_list):
        video_name_list = glob.glob(f'{single_sentence_video_dir}/*.mp4')

        for video_idx, video_path in enumerate(video_name_list):
            num_frames, fps = read_video(video_path)

            info = "{0}：视频帧率{1}，视频帧数{2}\n".format(video_path, fps, num_frames)

            with open("statistics.txt", "a+") as f:
                f.write(info)


if __name__ == '__main__':
    root_dir = r"/home/chenj0g/fps25_video4"
    read_all_video(root_dir)
