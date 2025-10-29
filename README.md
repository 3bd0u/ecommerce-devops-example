ecommerce-devops-example/

├─ app/                
│  ├─ app.py                     
│  ├─ requirements.txt                                                                              
│  ├─ models.py                                                                
│  ├─ routes.py                                     
│  └─ tests/                                                         
│                   ├─ test_api.py                                                                    
│                   └─ conftest.py                                                        
├─ Dockerfile                              
├─ docker-compose.yml                                        
├─ Jenkinsfile                                            
├─ deploy.sh                                        
├─ k8s/                                                   
│  ├─ deployment.yaml                                                    
│  ├─ service.yaml                                                               
│  └─ ingress.yaml                                                                    
├─ terraform/                                  
│  ├─ main.tf                           
│  ├─ variables.tf                                    
│  └─ outputs.tf                                 
├─ ansible/                                           
│  ├─ inventory.ini                                       
│  └─ playbooks/                                       
│     └─ setup_server.yml                                 
├─ monitoring/                                              
│  ├─ prometheus.yml                                     
│  └─ grafana_dashboard.json                                       
├─ README.md                                           
└─ .gitignore                                            
