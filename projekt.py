import Leap, sys, math
from Leap import SwipeGesture,Arm


class LeapMotionListener(Leap.Listener):
    def on_connect(self, controller):
        print("Uspjesno spojeno")
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        
    def on_frame(self, controller):
        frame=controller.frame()

        for gesture in frame.gestures():
            if(gesture.type==Leap.Gesture.TYPE_SWIPE):
                swipe=SwipeGesture(gesture)
                swipeDir=swipe.direction
                if(swipeDir.x > 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
                    print("Swiped desno")
                elif(swipeDir.x < 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
                    print("Swiped livo")
                elif(swipeDir.y > 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
                    print("Swiped gore")
                elif(swipeDir.y < 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
                    print("Swiped dole")

        for hand in frame.hands:
            HandType="Liva" if  hand.is_left else "Desna"
            print("ruka:"+ HandType + "Zglob:"+ str(hand.palm_position))





def main():
    listener=LeapMotionListener()
    controller=Leap.Controller()
    
    controller.add_listener(listener)

    print("Enter za kraj")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)
    
    
if __name__=="__main__":
    main()