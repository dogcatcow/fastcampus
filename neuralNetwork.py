# 업데이트 중. 예상 종료 시점: 2019.6. 이전

import numpy
import scipy.special
class neuralNetwork:

    # S3: 아래서 매개변수 받아서 '객체(self)에 라벨링' 해주기. ~호출 간소화 목적? (to) n.inodes 필기.
    # 라벨링 시 '우변' 부터 먼저 적는 습관.   ex: self.label ?

    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.lr = learningrate

        # 메소드서, 넘겨받는 매변?: (mean, spread, output shape)
        # if given (m, n, k), then output shape: m * n * k ... 행렬곱? ~곱집합?
        # pow(self.hnodes,-0.5) : 노드로 들어오는 연결노드의 개수에 루트 씌우고(0.5) 역수 취함. ( (-)부분, pow )
        self.wih = numpy.random.normal(0.0, pow(self.hnodes,-0.5), (self.hnodes,self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        self.activation_function = lambda x:  scipy.special.expit(x)    # lambda y ... expit(y)해도 됨?

        pass

# S1: 매개변수?...에 인자?를 넣기? 매개변수 != 인자
input_nodes = 3
hidden_nodes = 3
output_nodes = 3

learning_rate = 0.3


# S2:결국 이게...매변?에 들가고, 매변이 객체에 들감?
# 클래스는 객체 생성자(메소드?)...매변을 넘겨받아 객체를 만드는?
n = neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)


#객체지향 프로그래밍: 객체 단위로 데이터(필드?)와 기능(function,메소드?) 를 하나로 묶어 쓰는 방식.
#-> ex: n.inodes 하면 필드 호출. n.(아래 정의할 메소드 이름) 하면 메소드 호출... 객체('n' 단위)로 필드,메소드 다 갖다 쓰기?



# 신경망 학습시키기
    def train():   #매개변수값 무, 리턴값 무? Cf. Java
        pass


# 신경망에 질의하기
    def query(self, inputs_list)    # 1) 이 행에서 매변 선언하고.

        # 입력 리스트를 2차원 행렬로 변환
        # numpy array
        inputs = numpy.array(inputs_list, ndmin=2).T      # 2) 이 행에서 매변...을 특정 변수(좌변)에 넣어 줌. 왜 전치? (82)
                                                          # ndmin=2 : min dimension: 2. why T?
        hidden_inputs = numpy.dot(self.wih, inputs)       # 은닉입. 2차원이니 dot product -> 행렬곱.   wih: weight

        #[입력->은닉, ih] 신호 계산? 즉 은닉계층에서 Xhidden 나오면, 활성화함수에 집어넣음. O(Xhidden).
        hidden_outputs = self.activation_function(hidden_inputs)   # 은닉출.

        final_inputs = numpy.dot(self.who, hidden_outputs)        # 출력입

        final_outputs = self.activation_function(final_inputs)  # 출력출.

        return final_outputs                                    # 원노트 필기와 대조. 코딩 옆에 수학 기호 Wjk, Ok 등 붙이기

 '''
 # Parts: 초기화, 학습, 질의 (176)
# P1: 신경망 클래스 초기화. (붕어빵틀 만들기) 
class Re_NeuralNet:
    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):         
        # 각 계층 노드개수 초기화 부분? 필드는 P3에서 호출? ...(to) P3.
        #-> 매개변수를 매개로 메소드 안에 인자가 들어온다? ...우변부터 쓰는 연습?
        #-> 인자(실제전달되는 값) --> [  ]  매개변수 --> {   }메소드  ?   
        
        self.inodes = inputnodes   # 매개변수 우변을 매개로, 인자가 self.inodes에 담김?
                                   # -> inodes는 P3의 객체 'n'에 붙는 ~라벨? (Cf. 라벨링) 
        self.hnodes = hiddennodes  # 랜덤값으로 가중치 초기화할 것임. 
                                   # -> 노드가 많을수록, 가중치 범위를 줄여야. (포화 방지)...(138)
        self.onodes = outputnodes  # --> x좌표상 Wjk (+)or(-) 향할때, 편향 가능성. Y축 E 
        
        self.wih = numpy.random.normal(  0.0,  pow(self.hnodes,-0.5),  (self.hnodes,self.inodes)  )   # (88)
        self.who = numpy.random.normal(  0.0,  pow(self.hnodes,-0.5),  (self.hnodes,self.inodes)  )   # (88)
        
        #가중치를 무작위로 뽑는 방법 ex: numpy.random.rand(3,3)  ... 랜덤 3*3 matrix
        #가우스 분포에서 무작위로 뽑는 방법 numpy.random.normal(x,y,z)...곱집합 2개?
        
        
        #-> EX:은닉(j)->출력(k), 들어오는 노드(입력i, 은닉h) 3개 경우. 
        #--> 가중치 초기값: -1/sqrt3...0(mean)...+1/sqrt3, 
        #편향억제1) 3이 역수로 들감. 많을수록 초기값 작아짐. 편향억제2) sqrt로 제곱역연산.
        
        # self.inodes는 그냥 매변의 라벨링? 
        # 어쨌든 normal( x, y, z)에서, z는. output shape. 곱집합 모양임. 
        # pow(self.hnodes,-0.5) : 노드로 들어오는 연결노드의 개수에 루트 씌우고(0.5) 역수 ^(-) 취함. 
        
        self.lr = learningrate   #P3에서 넘겨받기?
        
        self.activation_function = lambda x: scipy.special.expit(x)   # 함수 호출해 쓰도록 변수 선언.
        
        pass

#P2?: 신경망에 질의하기    
    
    def query(self, inputs_list):  # 매변 targets_list 넣기 전 모델. (186)
        inputs = numpy.array(inputs_list, ndmin=2).T  # 리스트에 든 입력값을 2차원으로 강제 변경. n * 1 형식? (87)
                                                      # Cf. 입력값은 픽셀값.    
        hidden_inputs = numpy.dot(self.wih, inputs)   # 입력 출->은닉 입. (82)?  dot: 곱집합? 행렬곱? (89) wih: (88)
        hidden_outputs = self.activation_function(hidden_inputs) # (90)
        final_inputs = numpy.dot(self.who, hidden_outputs) #은닉 출->출력 입. 
        final_outputs = self.activation_function(final_inputs)           #여기서도 self 사용. 여전히 클래스 코드블록 안임. 
        
        return final_outputs
    
    
    
    
    
#P3?: 신경망 학습시키기..[full size]
#    def train(self, inputs_list, targets_list):
                                              # numpy array, by default: (784, ) . By ndmin=2:  (784,1)...forced 2nd dim.
 #       inputs = numpy.array(inputs_list, ndmin=2).T      #inputs_list: 784 pixel values (label 뺀값)
                                                          #training data(785 values): label + 784 pixel values (28*28)..?   
                                                          #Only if   
        
   '''     
    



    
    
    
       
