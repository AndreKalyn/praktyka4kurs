import math

class Segment:
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @staticmethod
    def calculate_angle(seg1, seg2) -> float:
        # Calculate the vectors representing the line segments
        vector1 = (seg1.x2 - seg1.x1, seg1.y2 - seg1.y1)
        vector2 = (seg2.x2 - seg2.x1, seg2.y2 - seg2.y1)

        # Calculate the dot product and the magnitudes of the vectors
        dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
        magnitude1 = math.sqrt(vector1[0] ** 2 + vector1[1]**2)
        magnitude2 = math.sqrt(vector2[0] ** 2 + vector2[1]**2)

        # Calculate the cosine of the angle using the dot product and magnitudes
        cosine_angle = dot_product / (magnitude1 * magnitude2)

        # Calculate the angle in radians
        angle_rad = math.acos(cosine_angle)

        # Convert the angle to degrees
        angle_deg = math.degrees(angle_rad)

        return angle_deg
        

def main():
    x1 = float(input("Enter x of point A: "))
    y1 = float(input("Enter y of point A: "))
    x2 = float(input("Enter x of point B: "))
    y2 = float(input("Enter y of point B: "))

    OA = Segment(0, 0, x1, y1)
    OB = Segment(0, 0, x2, y2)
    OX = Segment(0, 0, 1, 0)

    OA_OX_angle = Segment.calculate_angle(OA, OX)
    OB_OX_angle = Segment.calculate_angle(OB, OX)

    if (OA_OX_angle > OB_OX_angle):
        print("OA", OA_OX_angle)
    else:
        print("OB", OB_OX_angle)

if __name__ == "__main__":
    main()