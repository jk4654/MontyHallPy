
import random

def total():
    global Change_car_count
    global Change_goat_count
    global notChange_car_count
    global notChange_goat_count
    Change_car_count = 0
    Change_goat_count = 0
    notChange_car_count = 0
    notChange_goat_count = 0
    
    IfChange()
    IfNotChange()

def IfChange():
    global Change_car_count
    global Change_goat_count
    for i in range(0,100000):
        items = ['car','goat','goat']   # 3개의 문
        random.shuffle(items)           # 문을 섞음

        choice_index = random.randint(0,2)  # 3개의 문들 중에서 하나를 선택함
        del items[choice_index]        # 선택한 문을 지움
        found = items.index('goat')    # 나머지 문 중에서 염소가 있는 문 중에 하나를 골라서
        del items[found]               # 지움       
        final_choice = items[0]        # 처음 선택한 문과 사회자가 공개한 문을 제외한 나머지 문을 최종 선택
        
        if(final_choice == 'car'):
            Change_car_count = Change_car_count + 1
        elif (final_choice == 'goat'):
            Change_goat_count = Change_goat_count + 1

    print('바꿨을 때 자동차가 나온 횟수: ' + str(Change_car_count))
    print('바꿨을 때 염소가 나온 횟수: ' + str(Change_goat_count))
    print('>>바꿨을 때 자동차가 나올 확률: ' + str(Change_car_count/(Change_car_count + Change_goat_count)*100 )+ '%')

def IfNotChange():
    global notChange_car_count
    global notChange_goat_count
    for i in range(0,100000):
        items = ['car','goat','goat']   # 3개의 문
        random.shuffle(items)           # 문을 섞음

        choice_index = random.randint(0,2)  # 3개의 문들 중에서 하나를 선택함
        final_choice = items[choice_index]  # 그것을 최종 선택

        if(final_choice == 'car'):
            notChange_car_count = notChange_car_count + 1
        elif (final_choice == 'goat'):
            notChange_goat_count = notChange_goat_count + 1

    print('---')
    print('안 바꿨을 때 자동차가 나온 횟수: ' + str(notChange_car_count))
    print('안 바꿨을 때 염소가 나온 횟수: ' + str(notChange_goat_count))
    print('>>안 바꿨을 때 자동차가 나올 확률: ' + str(notChange_car_count/(notChange_car_count + notChange_goat_count)*100 )+ '%')
total()











