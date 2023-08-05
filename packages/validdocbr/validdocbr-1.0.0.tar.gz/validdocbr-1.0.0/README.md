validdocbr   
    
Document validator (CPF or CNPJ) based on the verification digit.     
   
Installation   
   
    pip install validdocbr   
   
Usage      
Send a CNPJ or CPF as a string (may contain special characters), it can contain special characters, returns True if the document is valid or False if it is invalid, using the check digits for the conference.     
    
Example:     
     
import validdocbr    
     
cpf = "12345678912"    
cnpj = "98765432112345"    
      
validdocbr.cpf (cpf_valid) ---> to validate CPF      
validdocbr.cnpj (cpf_valid) ---> to validate CNPJ     
        
answer = False ---> if the document is invalid      
answer = True ---> if the document is valid      
    
    
--------------------------------------------------------------------------------------------------------------------------------------------
   
   
validdocbr   
   
Validador de documentos (CPF ou CNPJ) com base no digito verificador.   
   
Istalação   
   
    pip install validdocbr
   
Utilização   
Ennvie um CNPJ ou CPF como string (pode conter caracteres especiais), pode conter caracteres especiais, retorna True se documento for válido ou False caso seja inválido, utilizando os digitos verificadores para conferencia.       

Exemplo:      

import validdocbr      
 
cpf = "12345678912"      
cnpj = "98765432112345"     
    
validdocbr.cpf(cpf_valid) ---> para validar CPF      
validdocbr.cnpj(cpf_valid) ---> para validar CNPJ      

resposta = False ---> caso documento seja inválido      
reposta = True ---> caso docmunto seja válido     
