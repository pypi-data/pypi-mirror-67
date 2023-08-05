# validdocbr   
    
* Document validator (CPF or CNPJ) based on the verification digit.     
   
Installation:   
```
pip install validdocbr   
pip3 install validdocbr   
```   
# Usage:      
* Send a CNPJ or CPF as a string, it can contain special characters, returns True if the document is valid or False if it is invalid, using the check digits for the conference.     
    
# Example:     
```     
from validdocbr import validdocbr
validator = validdocbr.validdocbr()
     
cpf = "12345678912"    
cnpj = "98765432112345"    
      
validator.cpf (cpf) ---> to validate CPF      
validator.cnpj (cnpj) ---> to validate CNPJ     
       
answer = False ---> the document is invalid      
answer = True ---> the document is valid      
```    
    
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
   
   
# validdocbr   
   
* Validador de documentos (CPF ou CNPJ) com base no digito verificador.   
   
# Istalação:   
   
```   
pip install validdocbr
pip3 install validdocbr
```
   
# Utilização:   
* Ennvie um CNPJ ou CPF como string, pode conter caracteres especiais, retorna True se documento for válido ou False caso seja inválido, utilizando os digitos verificadores para conferencia.       

# Exemplo:      
```
from validdocbr import validdocbr

validator = validdocbr.validdocbr()   
 
cpf = "12345678912"      
cnpj = "98765432112345"     
    
validador.cpf(cpf) ---> para validar CPF      
validador.cnpj(cnpj) ---> para validar CNPJ      

resposta = False ---> caso documento seja inválido      
reposta = True ---> caso docmunto seja válido     
```
