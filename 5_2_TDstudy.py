###라이브러리 import
import random


###GridWorld 클래스
class GridWolrd():
    def __init__(self):
        self.x = 0
        self.y = 0

    def step(self, a):
        if a == 0:
            self.move_right()
        elif a == 1:
            self.move_left()
        elif a == 2:
            self.move_up()
        elif a == 3:
            self.move_down()

        reward = -1
        done = self.is_done()
        return (self.x, self.y), reward, done
    
    def move_right(self):
        self.y += 1
        if self.y > 3:
            self.y = 3

    def move_left(self):
        self.y -= 1
        if self.y < 0:
            self.y = 0

    def move_up(self):
        self.x -= 1
        if self.x < 0:
            self.x = 0

    def move_down(self):
        self.x += 1
        if self.x > 3:
            self.x = 3

    def is_done(self):
        if self.x == 3 and self.y == 3:
            return True
        else:
            return False
        
    def get_state(self):
        return (self.x, self.y)
    
    def reset(self):
        self.x = 0
        self.y = 0
        return (self.x, self.y)
    

###Agent 클래스
class Agent():
    def __init__(self):
        pass
    
    def select_action(self):
        coin = random.random()
        if coin < 0.25:
            action = 0
        elif coin < 0.5:
            action = 1
        elif coin < 0.75:
            action =2
        else:
            action = 3
        return action
    

###메인 함수
def main():
    env = GridWolrd()
    agent = Agent()
    data = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #테이블 초기화
    gamma = 1.0
    alpha = 0.01 #MC에 비해 큰 값을 사용

    for k in range(50000): #총 5만 번의 에피소드 진행
        done = False
        while not done:
            x, y = env.get_state()
            action = agent.select_action()
            (x_prime, y_prime), reward, done = env.step(action)
            x_prime, y_prime = env.get_state()

            #한 번의 step이 진행됮 마자 바로 테이블의 데이터를 업데이트 해줌
            data[x][y] = data[x][y] + alpha*(reward+gamma*data[x_prime][y_prime]-data[x][y])
        env.reset()

    #학습이 끝나고 난 후 데이터를 출력해보기 위한 코드
    for row in data:
        print(row)


main()
