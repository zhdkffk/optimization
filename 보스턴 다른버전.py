from sklearn.datasets import load_boston
import pandas as pd
import statsmodels.formula.api as sm

#보스턴 집값으로 선형회귀!

#기울기 구하기
#"기울기를 계속 바꿔가면서(=경우의 수를 모두 찾아서) 최적의 기울기를 찾기 - 오차가 최소 --- 절편 안 구했음
#주의 사항: 분모는 0이 되면 안 됨, 분자는 음수를 체크할 필요가 없음, 분자가 0이면 절편이 없으므로 항상 최저값이 나올 수 있음
boston_data = load_boston()
boston = pd.DataFrame(data=boston_data.data, columns=boston_data.feature_names)
boston['target'] = boston_data.target

train = boston.sample(frac=0.8, random_state=200)
test = boston.drop(train.index)

result = sm.glm(formula= 'target ~ CRIM + ZN + CHAS + NOX + RM  + DIS + RAD + TAX + PTRATIO + B + LSTAT', data=train).fit()

print(result.summary())
sum_difference = 0
for i, row in test.iterrows():
    params = result.params
    r_estimate = row['PTRATIO'] * params['PTRATIO'] + row['NOX'] * params['NOX'] + row['B'] * params['B'] + row['CHAS'] * params['CHAS'] + \
                 row['RAD'] * params['RAD'] + row['TAX'] * params['TAX'] + row['ZN'] * params['ZN'] + row['DIS'] * params['DIS'] + \
                 row['CRIM'] * params['CRIM'] + row['RM'] * params['RM'] + row['LSTAT'] * params['LSTAT'] + params['Intercept']

    difference = abs(row['target'] - r_estimate)
    sum_difference += difference

print(sum_difference)

#시행착오
#실제보다 너무 기울기의 절댓값이 큼
#데이터를 보정하자

#결국 y절편이 필요! 최소제곱법을 사용하자 - 유도 과정이 필요없음


