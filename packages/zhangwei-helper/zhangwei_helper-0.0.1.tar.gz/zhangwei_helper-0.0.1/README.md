#zhangwei_helper
zhangwei_helper is a package include all common part,like function,enum,written \
by zhang wei(zwzw911)    
## install    
`pip install zhangwei-helper`    
## content    
### enum    
SelfEnum    
***description***: a module include self defined enum   
***usage***:     
import zhangwei_helper.SelfEnum as self_enum  
1. CpuBits: bits64/bits32    
2. OsType: Windows/Linux    
3. WindowsVersion: Windows7/Windows8/Windows10/Unknown    
4. WindowsBits: Win32/Win64    
5. PythonVersion: Python2/Python3/Unknown    
6. ProxyType: Transparent/Anonymous/High_anonymous    
7. BrowserType: FireFox/Chrome/All    
   
### function     
**os**     
***description***: a module include some functions about os   
***usage***:   
import zhangwei_helper.Os as self_os     
1. get_cpu_bits(): 枚举(CpuBits)：cpu的位数    
2. get_os_type(): 枚举(OsType)：os的类型：windows或者linux    
3. get_windows_ver(): 枚举(WindowsVersion)：windows的版本（7/8/10）    
4. get_windows_bits(): 枚举(WindowsBits)：windows的位数：32或者64    
5. windows_login_as_admin(): Boolean：当前是否以admin登录    
6. get_python_major_version():枚举(PythonVersion)：返回python的大版本号：2或者3或者unknown 

**windows_**     
***description***: a module include some functions about os     
***usage***:    
import zhangwei_helper.WindowsServices as win_ser   
1. if_service_exists(): Boolean：服务是否存在    
2. if_service_running(): Booleans:服务是否运行    
 
  

### change history
0.0.1  add SelfEnum/Os/WindowsServices    