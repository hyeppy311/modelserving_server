# FastAPI를 이용한 딥러닝 모델 인퍼런스 API 서버   

## 프로젝트 소개   
수시로 변화하는 딥러닝 모델을 서빙하기 위한 모델 인퍼런스를 서빙하는 서버를 만든다.    
v2 프로토콜 딥러닝 모델 서빙, 모델 조회, 모델 버전 조회 등의 기능을 구현한다. 


## 배포 주소 
http://13.124.163.106/v2/    
  
### **REST API**    
```
v2/models/{model_name}/live/   
v2/models/{model_name}/ready/   
v2/   
v2/models/{model_name}/   
v2/models/{model_name}/versions/{model_version}/infer   
```   
model_name : gpt2

----------
## 개발도구    
* FastAPI    
* Docker    
* AWS EC2   
* Nginx   
