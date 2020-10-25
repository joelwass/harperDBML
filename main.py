from sklearn.linear_model import LinearRegression
import harperdb

url="<harper_instance_url>"
db = harperdb.HarperDB(
  url=url,
  username="readonlyUser",
  password="<testpassword>"
)

input_data = db.sql("SELECT temperature,clouds,confidence,rain from testSchema.inputData")
output_data = db.sql("SELECT skydiving from testSchema.outputData")

# Transform the data into an array of arrays [[90,0,0,8], [100,1,1,6]]
TRAIN_INPUT = []
TRAIN_OUTPUT = []

for i in input_data:
  TRAIN_INPUT.append([i['temperature'], i['clouds'], i['rain'], i['confidence']])

# transform output as well
for z in output_data:
  TRAIN_OUTPUT.append([z['skydiving']])

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT,y=TRAIN_OUTPUT)

X_TEST=[[90,0,0,9]]
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_
print('Outcome: : {}\nCoefficients: {}'.format(outcome, coefficients))


