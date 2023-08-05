import pandas as pd
class Hello():
    def __init__(self):
        self.test = 'welcome!'

    def output(self):
        df = pd.DataFrame({'first':[1,2,3],
                           'seconde':[6,7,8],
                           'third':[9,0,5]})
        print(df)
        return self.test

if __name__ == '__main__':
    a = Hello()
    a.output()