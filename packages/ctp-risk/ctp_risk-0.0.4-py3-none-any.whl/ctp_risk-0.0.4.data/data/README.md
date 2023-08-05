# ctp_risk_api

#### 项目介绍
风控接口封装

#### 软件架构
软件架构说明


#### 安装教程

* 官方文档 FtdcRiskUserApiStruct 需增加 #include <string> 否则报错

#### 使用说明

* 修改g_c.py中的 src_dir = '../riskapi_32' 编译32or64位dll
* 生成的py_enum.py需进一步处理
```python
class TShfeFtdcOptionsTypeType(Enum):
    """期权类型类型"""
    SHFE_FTDC_CP_CallOptions = 49
    """看涨"""
    SHFE_FTDC_CP_PutOptions = 50
    """看跌"""
    SHFE_FTDC_CP_NULL = 0
    SHFE_FTDC_CP_NotOptions2 = 48 # 增加
    """非期权"""

class TShfeFtdcMD5Type(Enum):
    """MD5校验码类型"""
    SHFE_FTDC_MD5_NULL = 0 # 增加

class TShfeFtdcCombinationTypeType(Enum):
    """组合类型类型"""
    SHFE_FTDC_COMBT_Future = 48
    """期货组合"""
    SHFE_FTDC_COMBT_BUL = 49
    """垂直价差BUL"""
    SHFE_FTDC_COMBT_BER = 50
    """垂直价差BER"""
    SHFE_FTDC_COMBT_STD = 51
    """跨式组合"""
    SHFE_FTDC_COMBT_STG = 52
    """宽跨式组合"""
    SHFE_FTDC_COMBT_PRT = 53
    """备兑组合"""
    SHFE_FTDC_COMBT_CLD = 54
    """时间价差组合"""
    SHFE_FTDC_COMBT_NULL = 0
    SHFE_FTDC_COMBT_Other = 55 # 增加
    """新增的未知类型"""
    SHFE_FTDC_COMBT_Other2 = 56 # 增加
    """新增的未知类型2"""
```
* 生成
  * linux
    ```bash
    g++ -shared -fPIC -o ./riskapi.so ./trade.cpp ./libriskuserapi.so
    ```

#### 32位与64位C++文件区别
* 32位需声明 WINAPI __cdecl