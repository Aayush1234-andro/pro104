import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (60, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1.5,
            (0, 0, 255)
            )
cv2.putText(img,
            "Mercury",
            (130, 250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255, 255, 255)
            )
cv2.putText(img,
            "Venus",
            (205, 255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255, 255, 255)
            )
cv2.putText(img,
            "Earth",
            (300, 255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255, 255, 255)
            )
cv2.putText(img,
            "Moon",
            (350, 175),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255, 255, 255)
            )
cv2.putText(img,
            "Mars",
            (390, 250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255, 255, 255)
            )
cv2.putText(img,
            "Jupiter",
            (600, 375),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255, 255, 255)
            )
cv2.putText(img,
            "Saturn",
            (775, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255, 255, 255)
            )
cv2.putText(img,
            "Uranus",
            (985, 290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255, 255, 255)
            )
cv2.putText(img,
            "Neptune",
            (1125, 285),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255, 255, 255)
            )
cv2.imshow("output", img)
cv2.waitKey(0)