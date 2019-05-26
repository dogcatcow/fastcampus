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
