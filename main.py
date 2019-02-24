import os
import tkinter.filedialog
import cv2


def main():
    root = tkinter.Tk()
    root.withdraw()
    file_type = [("file", ".ppm")]
    idir = os.path.abspath(os.path.dirname(__file__))
    file = tkinter.filedialog.askopenfilename(filetypes=file_type,
                                              initialdir=idir)
    base_img = cv2.imread("base.png", 1)

    f = open(file)
    ppm = f.readlines()
    f.close()

    res = ppm[1].replace("\n", "")
    w, h = map(int, res.split())

    ppm_to_png(w, h, ppm, base_img)


def ppm_to_png(w, h, ppm, base_img):
    bi = cv2.resize(base_img, (w, h))
    count = 0
    for i in range(h):
        for j in range(w):
            r, g, b = map(int, ppm[count + 3].split())
            bi[i, j] = (b, g, r)
            count += 1

    cv2.imwrite("result.png", bi)


if __name__ == "__main__":
    main()
