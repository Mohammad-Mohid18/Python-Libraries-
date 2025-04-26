import pandas as pd

data = [
        {'Student': 'john', 'science': 85,'maths': 75,'english':90},
        {'Student': 'joe', 'science': 87,'maths': 77,'english':60},
        {'Student': 'jane', 'science': 92,'maths': 88,'english':95},
        ]
# Pandas format is not similar to this.

# print(data)
df = pd.DataFrame(data)
print(df)


smart_data = {
    'Student': ['john', 'joe', 'jane'],
    'Science': [85, 87, 92],
    'Maths': [75, 77, 88],
    'English': [90, 60, 95]
}
#Pandas formnatis simiar to this.

# print(smart_data)
df = pd.DataFrame(smart_data)
print(df)