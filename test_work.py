from fastapi.testclient import TestClient
from API import app


client = TestClient(app)




    #assert response.json() == {"message": "Hello World"}
    # message  == setosa
    
def test_read_predict_set():
        response = client.post("/predict/",json={"sepal_length": 4.4, 
                                                 "sepal_width": 3.3, 
                                                 "petal_length": 2.2, 
                                                 "petal_width": 1.2})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data['prediction'] == 'setosa'

def test_read_predict_virginica():
        response = client.post("/predict/",json={"sepal_length": 5.9, 
                                                 "sepal_width": 3, 
                                                 "petal_length": 5.1, 
                                                 "petal_width": 1.8})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data['prediction'] == 'virginica'

def test_read_predict_versicolor():
        response = client.post("/predict/",json={"sepal_length": 4, 
                                                 "sepal_width": 3.2, 
                                                 "petal_length": 4, 
                                                 "petal_width": 1})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data['prediction'] == 'versicolor'        
