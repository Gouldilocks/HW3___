import threading
from time import sleep
from random import randint

class student:
  def __init__(self, num, in_room=False):
    self.num = num
    self.in_room = False
    self.done = False
    self.working = False
    self.thread = threading.Thread(target=self.run)

  def getInChair(self):
    self.thread.start()

  def run(self):
    sleep(randint(0,2))
    if self.in_room:
      print(self.num, " is in the room")
    else:
      print(self.num, " is waiting in a chair")

  def runHelp(self):
    sleep(randint(1,5))
    self.done = True
    print(self.num, " was helped")

  def giveHelp(self):
    self.thread.join()
    self.working = True
    self.thread = threading.Thread(target=self.runHelp)
    self.thread.start()
    # self.thread.join()


class chair:
  def __init__(self) -> None:
    self.taken = False
    self.student = None

  def take(self, newStudent) -> None:
    self.taken = True
    self.student = newStudent
    self.student.getInChair()

  def release(self) -> None:
    self.taken = False
    self.student = None


class hallway:
  def __init__(self) -> None:
    self.chairs = [chair(), chair(), chair()]

  def checkClear(self) -> bool:
    for chair in self.chairs:
      if chair.taken:
        return False
    return True

class ta:
  def __init__(self) -> None:
    self.sleeping = True
  
if __name__ == "__main__":
  room = chair()
  students = [student(i+1) for i in range(10)]
  hallway = hallway()
  ta = ta()
  while True:
    # ta will sleep if nobody in hallway or room
    ta.sleeping = hallway.checkClear() and not room.taken
    # If the ta is not sleeping
    if ta.sleeping:
      print("TA is sleeping")

    if not ta.sleeping:
      # Help the student in the room
      if not room.student.working:
        room.student.giveHelp()
      if room.student.done:
        room.release()
      # Check each of the chairs in the hallway
      for chair in hallway.chairs:
        # If the chair is taken by a student
        # print("looking at chair ", chair.student.num)
        if chair.taken:
          # print("chair taken by ", chair.student.num)
          if not chair.student.working:
            # print("helping ", chair.student.num)
            # Give help to that student
            chair.student.giveHelp()
            continue
          if chair.student.done:
            # print("student ", chair.student.num, " done")
            # Release that chair
            chair.release()
      # send the TA back to sleep if there is nobody
      ta.sleeping = hallway.checkClear() and not room.taken
      if ta.sleeping:
        print("TA is sleeping")

    # If there are no more students, end the program
    if len(students) == 0:
      break
    elif not room.taken:
      print("sending student to room")
      if ta.sleeping:
        print("TA is sleeping, and was woken up")
        ta.sleeping = False
      roomStudent = students.pop()
      roomStudent.in_room = True
      room.take(roomStudent)

    # Add students to the hallway and chairs
    if room.taken:
      for chair in hallway.chairs:
        if len(students) <= 0:
          break
        if not chair.taken:
          chair.take(students.pop())