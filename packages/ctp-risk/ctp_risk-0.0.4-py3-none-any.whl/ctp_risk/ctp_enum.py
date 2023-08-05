#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class TE_RESUME_TYPE(Enum):
	TERT_RESTART = 0
	TERT_RESUME = 1
	TERT_QUICK = 2


class TShfeFtdcExchangePropertyType(Enum):
    """交易所属性类型"""
    SHFE_FTDC_EXP_Normal = 48
    """正常"""
    SHFE_FTDC_EXP_GenOrderByTrade = 49
    """根据成交生成报单"""
    SHFE_FTDC_EXP_NULL = 0


class TShfeFtdcIdCardTypeType(Enum):
    """证件类型类型"""
    SHFE_FTDC_ICT_EID = 48
    """组织机构代码"""
    SHFE_FTDC_ICT_IDCard = 49
    """中国公民身份证"""
    SHFE_FTDC_ICT_OfficerIDCard = 50
    """军官证"""
    SHFE_FTDC_ICT_PoliceIDCard = 51
    """警官证"""
    SHFE_FTDC_ICT_SoldierIDCard = 52
    """士兵证"""
    SHFE_FTDC_ICT_HouseholdRegister = 53
    """户口簿"""
    SHFE_FTDC_ICT_Passport = 54
    """护照"""
    SHFE_FTDC_ICT_TaiwanCompatriotIDCard = 55
    """台胞证"""
    SHFE_FTDC_ICT_HomeComingCard = 56
    """回乡证"""
    SHFE_FTDC_ICT_LicenseNo = 57
    """营业执照号"""
    SHFE_FTDC_ICT_TaxNo = 65
    """税务登记号/当地纳税ID"""
    SHFE_FTDC_ICT_HMMainlandTravelPermit = 66
    """港澳居民来往内地通行证"""
    SHFE_FTDC_ICT_TwMainlandTravelPermit = 67
    """台湾居民来往大陆通行证"""
    SHFE_FTDC_ICT_DrivingLicense = 68
    """驾照"""
    SHFE_FTDC_ICT_SocialID = 70
    """当地社保ID"""
    SHFE_FTDC_ICT_LocalID = 71
    """当地身份证"""
    SHFE_FTDC_ICT_BusinessRegistration = 72
    """商业登记证"""
    SHFE_FTDC_ICT_HKMCIDCard = 73
    """港澳永久性居民身份证"""
    SHFE_FTDC_ICT_AccountsPermits = 74
    """人行开户许可证"""
    SHFE_FTDC_ICT_OtherCard = 120
    """其他证件"""
    SHFE_FTDC_ICT_NULL = 0


class TShfeFtdcInvestorRangeType(Enum):
    """投资者范围类型"""
    SHFE_FTDC_IR_All = 49
    """所有"""
    SHFE_FTDC_IR_Group = 50
    """投资者组"""
    SHFE_FTDC_IR_Single = 51
    """单一投资者"""
    SHFE_FTDC_IR_NULL = 0


class TShfeFtdcDepartmentRangeType(Enum):
    """投资者范围类型"""
    SHFE_FTDC_DR_All = 49
    """所有"""
    SHFE_FTDC_DR_Group = 50
    """组织架构"""
    SHFE_FTDC_DR_Single = 51
    """单一投资者"""
    SHFE_FTDC_DR_NULL = 0


class TShfeFtdcDataSyncStatusType(Enum):
    """数据同步状态类型"""
    SHFE_FTDC_DS_Asynchronous = 49
    """未同步"""
    SHFE_FTDC_DS_Synchronizing = 50
    """同步中"""
    SHFE_FTDC_DS_Synchronized = 51
    """已同步"""
    SHFE_FTDC_DS_NULL = 0


class TShfeFtdcBrokerDataSyncStatusType(Enum):
    """经纪公司数据同步状态类型"""
    SHFE_FTDC_BDS_Synchronized = 49
    """已同步"""
    SHFE_FTDC_BDS_Synchronizing = 50
    """同步中"""
    SHFE_FTDC_BDS_NULL = 0


class TShfeFtdcExchangeConnectStatusType(Enum):
    """交易所连接状态类型"""
    SHFE_FTDC_ECS_NoConnection = 49
    """没有任何连接"""
    SHFE_FTDC_ECS_QryInstrumentSent = 50
    """已经发出合约查询请求"""
    SHFE_FTDC_ECS_GotInformation = 57
    """已经获取信息"""
    SHFE_FTDC_ECS_NULL = 0


class TShfeFtdcTraderConnectStatusType(Enum):
    """交易所交易员连接状态类型"""
    SHFE_FTDC_TCS_NotConnected = 49
    """没有任何连接"""
    SHFE_FTDC_TCS_Connected = 50
    """已经连接"""
    SHFE_FTDC_TCS_QryInstrumentSent = 51
    """已经发出合约查询请求"""
    SHFE_FTDC_TCS_SubPrivateFlow = 52
    """订阅私有流"""
    SHFE_FTDC_TCS_NULL = 0


class TShfeFtdcFunctionCodeType(Enum):
    """功能代码类型"""
    SHFE_FTDC_FC_DataAsync = 49
    """数据异步化"""
    SHFE_FTDC_FC_ForceUserLogout = 50
    """强制用户登出"""
    SHFE_FTDC_FC_UserPasswordUpdate = 51
    """变更管理用户口令"""
    SHFE_FTDC_FC_BrokerPasswordUpdate = 52
    """变更经纪公司口令"""
    SHFE_FTDC_FC_InvestorPasswordUpdate = 53
    """变更投资者口令"""
    SHFE_FTDC_FC_OrderInsert = 54
    """报单插入"""
    SHFE_FTDC_FC_OrderAction = 55
    """报单操作"""
    SHFE_FTDC_FC_SyncSystemData = 56
    """同步系统数据"""
    SHFE_FTDC_FC_SyncBrokerData = 57
    """同步经纪公司数据"""
    SHFE_FTDC_FC_BachSyncBrokerData = 65
    """批量同步经纪公司数据"""
    SHFE_FTDC_FC_SuperQuery = 66
    """超级查询"""
    SHFE_FTDC_FC_ParkedOrderInsert = 67
    """预埋报单插入"""
    SHFE_FTDC_FC_ParkedOrderAction = 68
    """预埋报单操作"""
    SHFE_FTDC_FC_SyncOTP = 69
    """同步动态令牌"""
    SHFE_FTDC_FC_DeleteOrder = 70
    """删除未知单"""
    SHFE_FTDC_FC_NULL = 0


class TShfeFtdcBrokerFunctionCodeType(Enum):
    """经纪公司功能代码类型"""
    SHFE_FTDC_BFC_ForceUserLogout = 49
    """强制用户登出"""
    SHFE_FTDC_BFC_UserPasswordUpdate = 50
    """变更用户口令"""
    SHFE_FTDC_BFC_SyncBrokerData = 51
    """同步经纪公司数据"""
    SHFE_FTDC_BFC_BachSyncBrokerData = 52
    """批量同步经纪公司数据"""
    SHFE_FTDC_BFC_OrderInsert = 53
    """报单插入"""
    SHFE_FTDC_BFC_OrderAction = 54
    """报单操作"""
    SHFE_FTDC_BFC_AllQuery = 55
    """全部查询"""
    SHFE_FTDC_BFC_log = 97
    """系统功能：登入/登出/修改密码等"""
    SHFE_FTDC_BFC_BaseQry = 98
    """基本查询：查询基础数据，如合约，交易所等常量"""
    SHFE_FTDC_BFC_TradeQry = 99
    """交易查询：如查成交，委托"""
    SHFE_FTDC_BFC_Trade = 100
    """交易功能：报单，撤单"""
    SHFE_FTDC_BFC_Virement = 101
    """银期转账"""
    SHFE_FTDC_BFC_Risk = 102
    """风险监控"""
    SHFE_FTDC_BFC_Session = 103
    """查询/管理：查询会话，踢人等"""
    SHFE_FTDC_BFC_RiskNoticeCtl = 104
    """风控通知控制"""
    SHFE_FTDC_BFC_RiskNotice = 105
    """风控通知发送"""
    SHFE_FTDC_BFC_BrokerDeposit = 106
    """察看经纪公司资金权限"""
    SHFE_FTDC_BFC_QueryFund = 107
    """资金查询"""
    SHFE_FTDC_BFC_QueryOrder = 108
    """报单查询"""
    SHFE_FTDC_BFC_QueryTrade = 109
    """成交查询"""
    SHFE_FTDC_BFC_QueryPosition = 110
    """持仓查询"""
    SHFE_FTDC_BFC_QueryMarketData = 111
    """行情查询"""
    SHFE_FTDC_BFC_QueryUserEvent = 112
    """用户事件查询"""
    SHFE_FTDC_BFC_QueryRiskNotify = 113
    """风险通知查询"""
    SHFE_FTDC_BFC_QueryFundChange = 114
    """出入金查询"""
    SHFE_FTDC_BFC_QueryInvestor = 115
    """投资者信息查询"""
    SHFE_FTDC_BFC_QueryTradingCode = 116
    """交易编码查询"""
    SHFE_FTDC_BFC_ForceClose = 117
    """强平"""
    SHFE_FTDC_BFC_PressTest = 118
    """压力测试"""
    SHFE_FTDC_BFC_RemainCalc = 119
    """权益反算"""
    SHFE_FTDC_BFC_NetPositionInd = 120
    """净持仓保证金指标"""
    SHFE_FTDC_BFC_RiskPredict = 121
    """风险预算"""
    SHFE_FTDC_BFC_DataExport = 122
    """数据导出"""
    SHFE_FTDC_BFC_RiskTargetSetup = 65
    """风控指标设置"""
    SHFE_FTDC_BFC_MarketDataWarn = 66
    """行情预警"""
    SHFE_FTDC_BFC_QryBizNotice = 67
    """业务通知查询"""
    SHFE_FTDC_BFC_CfgBizNotice = 68
    """业务通知模板设置"""
    SHFE_FTDC_BFC_SyncOTP = 69
    """同步动态令牌"""
    SHFE_FTDC_BFC_SendBizNotice = 70
    """发送业务通知"""
    SHFE_FTDC_BFC_CfgRiskLevelStd = 71
    """风险级别标准设置"""
    SHFE_FTDC_BFC_TbCommand = 72
    """交易终端应急功能"""
    SHFE_FTDC_BFC_DeleteOrder = 74
    """删除未知单"""
    SHFE_FTDC_BFC_ParkedOrderInsert = 75
    """预埋报单插入"""
    SHFE_FTDC_BFC_ParkedOrderAction = 76
    """预埋报单操作"""
    SHFE_FTDC_BFC_ExecOrderNoCheck = 77
    """资金不够仍允许行权"""
    SHFE_FTDC_BFC_Designate = 78
    """指定"""
    SHFE_FTDC_BFC_StockDisposal = 79
    """证券处置"""
    SHFE_FTDC_BFC_BrokerDepositWarn = 81
    """席位资金预警"""
    SHFE_FTDC_BFC_CoverWarn = 83
    """备兑不足预警"""
    SHFE_FTDC_BFC_PreExecOrder = 84
    """行权试算"""
    SHFE_FTDC_BFC_ExecOrderRisk = 80
    """行权交收风险"""
    SHFE_FTDC_BFC_PosiLimitWarn = 85
    """持仓限额预警"""
    SHFE_FTDC_BFC_QryPosiLimit = 86
    """持仓限额查询"""
    SHFE_FTDC_BFC_FBSign = 87
    """银期签到签退"""
    SHFE_FTDC_BFC_FBAccount = 88
    """银期签约解约"""
    SHFE_FTDC_BFC_NULL = 0


class TShfeFtdcOrderActionStatusType(Enum):
    """报单操作状态类型"""
    SHFE_FTDC_OAS_Submitted = 97
    """已经提交"""
    SHFE_FTDC_OAS_Accepted = 98
    """已经接受"""
    SHFE_FTDC_OAS_Rejected = 99
    """已经被拒绝"""
    SHFE_FTDC_OAS_NULL = 0


class TShfeFtdcOrderStatusType(Enum):
    """报单状态类型"""
    SHFE_FTDC_OST_AllTraded = 48
    """全部成交"""
    SHFE_FTDC_OST_PartTradedQueueing = 49
    """部分成交还在队列中"""
    SHFE_FTDC_OST_PartTradedNotQueueing = 50
    """部分成交不在队列中"""
    SHFE_FTDC_OST_NoTradeQueueing = 51
    """未成交还在队列中"""
    SHFE_FTDC_OST_NoTradeNotQueueing = 52
    """未成交不在队列中"""
    SHFE_FTDC_OST_Canceled = 53
    """撤单"""
    SHFE_FTDC_OST_Unknown = 97
    """未知"""
    SHFE_FTDC_OST_NotTouched = 98
    """尚未触发"""
    SHFE_FTDC_OST_Touched = 99
    """已触发"""
    SHFE_FTDC_OST_NULL = 0


class TShfeFtdcOrderSubmitStatusType(Enum):
    """报单提交状态类型"""
    SHFE_FTDC_OSS_InsertSubmitted = 48
    """已经提交"""
    SHFE_FTDC_OSS_CancelSubmitted = 49
    """撤单已经提交"""
    SHFE_FTDC_OSS_ModifySubmitted = 50
    """修改已经提交"""
    SHFE_FTDC_OSS_Accepted = 51
    """已经接受"""
    SHFE_FTDC_OSS_InsertRejected = 52
    """报单已经被拒绝"""
    SHFE_FTDC_OSS_CancelRejected = 53
    """撤单已经被拒绝"""
    SHFE_FTDC_OSS_ModifyRejected = 54
    """改单已经被拒绝"""
    SHFE_FTDC_OSS_NULL = 0


class TShfeFtdcPositionDateType(Enum):
    """持仓日期类型"""
    SHFE_FTDC_PSD_Today = 49
    """今日持仓"""
    SHFE_FTDC_PSD_History = 50
    """历史持仓"""
    SHFE_FTDC_PSD_NULL = 0


class TShfeFtdcPositionDateTypeType(Enum):
    """持仓日期类型类型"""
    SHFE_FTDC_PDT_UseHistory = 49
    """使用历史持仓"""
    SHFE_FTDC_PDT_NoUseHistory = 50
    """不使用历史持仓"""
    SHFE_FTDC_PDT_NULL = 0


class TShfeFtdcTradingRoleType(Enum):
    """交易角色类型"""
    SHFE_FTDC_ER_Broker = 49
    """代理"""
    SHFE_FTDC_ER_Host = 50
    """自营"""
    SHFE_FTDC_ER_Maker = 51
    """做市商"""
    SHFE_FTDC_ER_NULL = 0


class TShfeFtdcProductClassType(Enum):
    """产品类型类型"""
    SHFE_FTDC_PC_Futures = 49
    """期货"""
    SHFE_FTDC_PC_Options = 50
    """期货期权"""
    SHFE_FTDC_PC_Combination = 51
    """组合"""
    SHFE_FTDC_PC_Spot = 52
    """即期"""
    SHFE_FTDC_PC_EFP = 53
    """期转现"""
    SHFE_FTDC_PC_SpotOption = 54
    """现货期权"""
    SHFE_FTDC_PC_NULL = 0


class TShfeFtdcInstLifePhaseType(Enum):
    """合约生命周期状态类型"""
    SHFE_FTDC_IP_NotStart = 48
    """未上市"""
    SHFE_FTDC_IP_Started = 49
    """上市"""
    SHFE_FTDC_IP_Pause = 50
    """停牌"""
    SHFE_FTDC_IP_Expired = 51
    """到期"""
    SHFE_FTDC_IP_NULL = 0


class TShfeFtdcDirectionType(Enum):
    """买卖方向类型"""
    SHFE_FTDC_D_Buy = 48
    """买"""
    SHFE_FTDC_D_Sell = 49
    """卖"""
    SHFE_FTDC_D_NULL = 0


class TShfeFtdcPositionTypeType(Enum):
    """持仓类型类型"""
    SHFE_FTDC_PT_Net = 49
    """净持仓"""
    SHFE_FTDC_PT_Gross = 50
    """综合持仓"""
    SHFE_FTDC_PT_NULL = 0


class TShfeFtdcPosiDirectionType(Enum):
    """持仓多空方向类型"""
    SHFE_FTDC_PD_Net = 49
    """净"""
    SHFE_FTDC_PD_Long = 50
    """多头"""
    SHFE_FTDC_PD_Short = 51
    """空头"""
    SHFE_FTDC_PD_NULL = 0


class TShfeFtdcSysSettlementStatusType(Enum):
    """系统结算状态类型"""
    SHFE_FTDC_SS_NonActive = 49
    """不活跃"""
    SHFE_FTDC_SS_Startup = 50
    """启动"""
    SHFE_FTDC_SS_Operating = 51
    """操作"""
    SHFE_FTDC_SS_Settlement = 52
    """结算"""
    SHFE_FTDC_SS_SettlementFinished = 53
    """结算完成"""
    SHFE_FTDC_SS_NULL = 0


class TShfeFtdcRatioAttrType(Enum):
    """费率属性类型"""
    SHFE_FTDC_RA_Trade = 48
    """交易费率"""
    SHFE_FTDC_RA_Settlement = 49
    """结算费率"""
    SHFE_FTDC_RA_NULL = 0


class TShfeFtdcHedgeFlagType(Enum):
    """投机套保标志类型"""
    SHFE_FTDC_HF_Speculation = 49
    """投机"""
    SHFE_FTDC_HF_Arbitrage = 50
    """套利"""
    SHFE_FTDC_HF_Hedge = 51
    """套保"""
    SHFE_FTDC_HF_MarketMaker = 53
    """做市商"""
    SHFE_FTDC_HF_NULL = 0


class TShfeFtdcBillHedgeFlagType(Enum):
    """投机套保标志类型"""
    SHFE_FTDC_BHF_Speculation = 49
    """投机"""
    SHFE_FTDC_BHF_Arbitrage = 50
    """套利"""
    SHFE_FTDC_BHF_Hedge = 51
    """套保"""
    SHFE_FTDC_BHF_NULL = 0


class TShfeFtdcClientIDTypeType(Enum):
    """交易编码类型类型"""
    SHFE_FTDC_CIDT_Speculation = 49
    """投机"""
    SHFE_FTDC_CIDT_Arbitrage = 50
    """套利"""
    SHFE_FTDC_CIDT_Hedge = 51
    """套保"""
    SHFE_FTDC_CIDT_MarketMaker = 53
    """做市商"""
    SHFE_FTDC_CIDT_NULL = 0


class TShfeFtdcOrderPriceTypeType(Enum):
    """报单价格条件类型"""
    SHFE_FTDC_OPT_AnyPrice = 49
    """任意价"""
    SHFE_FTDC_OPT_LimitPrice = 50
    """限价"""
    SHFE_FTDC_OPT_BestPrice = 51
    """最优价"""
    SHFE_FTDC_OPT_LastPrice = 52
    """最新价"""
    SHFE_FTDC_OPT_LastPricePlusOneTicks = 53
    """最新价浮动上浮1个ticks"""
    SHFE_FTDC_OPT_LastPricePlusTwoTicks = 54
    """最新价浮动上浮2个ticks"""
    SHFE_FTDC_OPT_LastPricePlusThreeTicks = 55
    """最新价浮动上浮3个ticks"""
    SHFE_FTDC_OPT_AskPrice1 = 56
    """卖一价"""
    SHFE_FTDC_OPT_AskPrice1PlusOneTicks = 57
    """卖一价浮动上浮1个ticks"""
    SHFE_FTDC_OPT_AskPrice1PlusTwoTicks = 65
    """卖一价浮动上浮2个ticks"""
    SHFE_FTDC_OPT_AskPrice1PlusThreeTicks = 66
    """卖一价浮动上浮3个ticks"""
    SHFE_FTDC_OPT_BidPrice1 = 67
    """买一价"""
    SHFE_FTDC_OPT_BidPrice1PlusOneTicks = 68
    """买一价浮动上浮1个ticks"""
    SHFE_FTDC_OPT_BidPrice1PlusTwoTicks = 69
    """买一价浮动上浮2个ticks"""
    SHFE_FTDC_OPT_BidPrice1PlusThreeTicks = 70
    """买一价浮动上浮3个ticks"""
    SHFE_FTDC_OPT_FiveLevelPrice = 71
    """五档价"""
    SHFE_FTDC_OPT_NULL = 0


class TShfeFtdcOffsetFlagType(Enum):
    """开平标志类型"""
    SHFE_FTDC_OF_Open = 48
    """开仓"""
    SHFE_FTDC_OF_Close = 49
    """平仓"""
    SHFE_FTDC_OF_ForceClose = 50
    """强平"""
    SHFE_FTDC_OF_CloseToday = 51
    """平今"""
    SHFE_FTDC_OF_CloseYesterday = 52
    """平昨"""
    SHFE_FTDC_OF_ForceOff = 53
    """强减"""
    SHFE_FTDC_OF_LocalForceClose = 54
    """本地强平"""
    SHFE_FTDC_OF_NULL = 0


class TShfeFtdcForceCloseReasonType(Enum):
    """强平原因类型"""
    SHFE_FTDC_FCC_NotForceClose = 48
    """非强平"""
    SHFE_FTDC_FCC_LackDeposit = 49
    """资金不足"""
    SHFE_FTDC_FCC_ClientOverPositionLimit = 50
    """客户超仓"""
    SHFE_FTDC_FCC_MemberOverPositionLimit = 51
    """会员超仓"""
    SHFE_FTDC_FCC_NotMultiple = 52
    """持仓非整数倍"""
    SHFE_FTDC_FCC_Violation = 53
    """违规"""
    SHFE_FTDC_FCC_Other = 54
    """其它"""
    SHFE_FTDC_FCC_PersonDeliv = 55
    """自然人临近交割"""
    SHFE_FTDC_FCC_NULL = 0


class TShfeFtdcOrderTypeType(Enum):
    """报单类型类型"""
    SHFE_FTDC_ORDT_Normal = 48
    """正常"""
    SHFE_FTDC_ORDT_DeriveFromQuote = 49
    """报价衍生"""
    SHFE_FTDC_ORDT_DeriveFromCombination = 50
    """组合衍生"""
    SHFE_FTDC_ORDT_Combination = 51
    """组合报单"""
    SHFE_FTDC_ORDT_ConditionalOrder = 52
    """条件单"""
    SHFE_FTDC_ORDT_Swap = 53
    """互换单"""
    SHFE_FTDC_ORDT_NULL = 0


class TShfeFtdcTimeConditionType(Enum):
    """有效期类型类型"""
    SHFE_FTDC_TC_IOC = 49
    """立即完成，否则撤销"""
    SHFE_FTDC_TC_GFS = 50
    """本节有效"""
    SHFE_FTDC_TC_GFD = 51
    """当日有效"""
    SHFE_FTDC_TC_GTD = 52
    """指定日期前有效"""
    SHFE_FTDC_TC_GTC = 53
    """撤销前有效"""
    SHFE_FTDC_TC_GFA = 54
    """集合竞价有效"""
    SHFE_FTDC_TC_NULL = 0


class TShfeFtdcVolumeConditionType(Enum):
    """成交量类型类型"""
    SHFE_FTDC_VC_AV = 49
    """任何数量"""
    SHFE_FTDC_VC_MV = 50
    """最小数量"""
    SHFE_FTDC_VC_CV = 51
    """全部数量"""
    SHFE_FTDC_VC_NULL = 0


class TShfeFtdcContingentConditionType(Enum):
    """触发条件类型"""
    SHFE_FTDC_CC_Immediately = 49
    """立即"""
    SHFE_FTDC_CC_Touch = 50
    """止损"""
    SHFE_FTDC_CC_TouchProfit = 51
    """止赢"""
    SHFE_FTDC_CC_ParkedOrder = 52
    """预埋单"""
    SHFE_FTDC_CC_LastPriceGreaterThanStopPrice = 53
    """最新价大于条件价"""
    SHFE_FTDC_CC_LastPriceGreaterEqualStopPrice = 54
    """最新价大于等于条件价"""
    SHFE_FTDC_CC_LastPriceLesserThanStopPrice = 55
    """最新价小于条件价"""
    SHFE_FTDC_CC_LastPriceLesserEqualStopPrice = 56
    """最新价小于等于条件价"""
    SHFE_FTDC_CC_AskPriceGreaterThanStopPrice = 57
    """卖一价大于条件价"""
    SHFE_FTDC_CC_AskPriceGreaterEqualStopPrice = 65
    """卖一价大于等于条件价"""
    SHFE_FTDC_CC_AskPriceLesserThanStopPrice = 66
    """卖一价小于条件价"""
    SHFE_FTDC_CC_AskPriceLesserEqualStopPrice = 67
    """卖一价小于等于条件价"""
    SHFE_FTDC_CC_BidPriceGreaterThanStopPrice = 68
    """买一价大于条件价"""
    SHFE_FTDC_CC_BidPriceGreaterEqualStopPrice = 69
    """买一价大于等于条件价"""
    SHFE_FTDC_CC_BidPriceLesserThanStopPrice = 70
    """买一价小于条件价"""
    SHFE_FTDC_CC_BidPriceLesserEqualStopPrice = 72
    """买一价小于等于条件价"""
    SHFE_FTDC_CC_NULL = 0


class TShfeFtdcActionFlagType(Enum):
    """操作标志类型"""
    SHFE_FTDC_AF_Delete = 48
    """删除"""
    SHFE_FTDC_AF_Modify = 51
    """修改"""
    SHFE_FTDC_AF_NULL = 0


class TShfeFtdcTradingRightType(Enum):
    """交易权限类型"""
    SHFE_FTDC_TR_Allow = 48
    """可以交易"""
    SHFE_FTDC_TR_CloseOnly = 49
    """只能平仓"""
    SHFE_FTDC_TR_Forbidden = 50
    """不能交易"""
    SHFE_FTDC_TR_NULL = 0


class TShfeFtdcOrderSourceType(Enum):
    """报单来源类型"""
    SHFE_FTDC_OSRC_Participant = 48
    """来自参与者"""
    SHFE_FTDC_OSRC_Administrator = 49
    """来自管理员"""
    SHFE_FTDC_OSRC_NULL = 0


class TShfeFtdcTradeTypeType(Enum):
    """成交类型类型"""
    SHFE_FTDC_TRDT_SplitCombinatio = 110
    """组合持仓拆分为单一持仓,初始化不应包含该类型的持仓"""
    SHFE_FTDC_TRDT_Common = 48
    """普通成交"""
    SHFE_FTDC_TRDT_OptionsExecution = 49
    """期权执行"""
    SHFE_FTDC_TRDT_OTC = 50
    """OTC成交"""
    SHFE_FTDC_TRDT_EFPDerived = 51
    """期转现衍生成交"""
    SHFE_FTDC_TRDT_CombinationDerived = 52
    """组合衍生成交"""
    SHFE_FTDC_TRDT_NULL = 0


class TShfeFtdcPriceSourceType(Enum):
    """成交价来源类型"""
    SHFE_FTDC_PSRC_LastPrice = 48
    """前成交价"""
    SHFE_FTDC_PSRC_Buy = 49
    """买委托价"""
    SHFE_FTDC_PSRC_Sell = 50
    """卖委托价"""
    SHFE_FTDC_PSRC_NULL = 0


class TShfeFtdcInstrumentStatusType(Enum):
    """合约交易状态类型"""
    SHFE_FTDC_IS_BeforeTrading = 48
    """开盘前"""
    SHFE_FTDC_IS_NoTrading = 49
    """非交易"""
    SHFE_FTDC_IS_Continous = 50
    """连续交易"""
    SHFE_FTDC_IS_AuctionOrdering = 51
    """集合竞价报单"""
    SHFE_FTDC_IS_AuctionBalance = 52
    """集合竞价价格平衡"""
    SHFE_FTDC_IS_AuctionMatch = 53
    """集合竞价撮合"""
    SHFE_FTDC_IS_Closed = 54
    """收盘"""
    SHFE_FTDC_IS_NULL = 0


class TShfeFtdcInstStatusEnterReasonType(Enum):
    """品种进入交易状态原因类型"""
    SHFE_FTDC_IER_Automatic = 49
    """自动切换"""
    SHFE_FTDC_IER_Manual = 50
    """手动切换"""
    SHFE_FTDC_IER_Fuse = 51
    """熔断"""
    SHFE_FTDC_IER_NULL = 0


class TShfeFtdcBatchStatusType(Enum):
    """处理状态类型"""
    SHFE_FTDC_BS_NoUpload = 49
    """未上传"""
    SHFE_FTDC_BS_Uploaded = 50
    """已上传"""
    SHFE_FTDC_BS_Failed = 51
    """审核失败"""
    SHFE_FTDC_BS_NULL = 0


class TShfeFtdcReturnStyleType(Enum):
    """按品种返还方式类型"""
    SHFE_FTDC_RS_All = 49
    """按所有品种"""
    SHFE_FTDC_RS_ByProduct = 50
    """按品种"""
    SHFE_FTDC_RS_NULL = 0


class TShfeFtdcReturnPatternType(Enum):
    """返还模式类型"""
    SHFE_FTDC_RP_ByVolume = 49
    """按成交手数"""
    SHFE_FTDC_RP_ByFeeOnHand = 50
    """按留存手续费"""
    SHFE_FTDC_RP_NULL = 0


class TShfeFtdcReturnLevelType(Enum):
    """返还级别类型"""
    SHFE_FTDC_RL_Level1 = 49
    """级别1"""
    SHFE_FTDC_RL_Level2 = 50
    """级别2"""
    SHFE_FTDC_RL_Level3 = 51
    """级别3"""
    SHFE_FTDC_RL_Level4 = 52
    """级别4"""
    SHFE_FTDC_RL_Level5 = 53
    """级别5"""
    SHFE_FTDC_RL_Level6 = 54
    """级别6"""
    SHFE_FTDC_RL_Level7 = 55
    """级别7"""
    SHFE_FTDC_RL_Level8 = 56
    """级别8"""
    SHFE_FTDC_RL_Level9 = 57
    """级别9"""
    SHFE_FTDC_RL_NULL = 0


class TShfeFtdcReturnStandardType(Enum):
    """返还标准类型"""
    SHFE_FTDC_RSD_ByPeriod = 49
    """分阶段返还"""
    SHFE_FTDC_RSD_ByStandard = 50
    """按某一标准"""
    SHFE_FTDC_RSD_NULL = 0


class TShfeFtdcMortgageTypeType(Enum):
    """质押类型类型"""
    SHFE_FTDC_MT_Out = 48
    """质出"""
    SHFE_FTDC_MT_In = 49
    """质入"""
    SHFE_FTDC_MT_NULL = 0


class TShfeFtdcInvestorSettlementParamIDType(Enum):
    """投资者结算参数代码类型"""
    SHFE_FTDC_ISPI_MortgageRatio = 52
    """质押比例"""
    SHFE_FTDC_ISPI_MarginWay = 53
    """保证金算法"""
    SHFE_FTDC_ISPI_BillDeposit = 57
    """结算单结存是否包含质押"""
    SHFE_FTDC_ISPI_NULL = 0


class TShfeFtdcExchangeSettlementParamIDType(Enum):
    """交易所结算参数代码类型"""
    SHFE_FTDC_ESPI_MortgageRatio = 49
    """质押比例"""
    SHFE_FTDC_ESPI_OtherFundItem = 50
    """分项资金导入项"""
    SHFE_FTDC_ESPI_OtherFundImport = 51
    """分项资金入交易所出入金"""
    SHFE_FTDC_ESPI_CFFEXMinPrepa = 54
    """中金所开户最低可用金额"""
    SHFE_FTDC_ESPI_CZCESettlementType = 55
    """郑商所结算方式"""
    SHFE_FTDC_ESPI_ExchDelivFeeMode = 57
    """交易所交割手续费收取方式"""
    SHFE_FTDC_ESPI_DelivFeeMode = 48
    """投资者交割手续费收取方式"""
    SHFE_FTDC_ESPI_CZCEComMarginType = 65
    """郑商所组合持仓保证金收取方式"""
    SHFE_FTDC_ESPI_DceComMarginType = 66
    """大商所套利保证金是否优惠"""
    SHFE_FTDC_ESPI_OptOutDisCountRate = 97
    """虚值期权保证金优惠比率"""
    SHFE_FTDC_ESPI_OptMiniGuarantee = 98
    """最低保障系数"""
    SHFE_FTDC_ESPI_NULL = 0


class TShfeFtdcSystemParamIDType(Enum):
    """系统参数代码类型"""
    SHFE_FTDC_SPI_InvestorIDMinLength = 49
    """投资者代码最小长度"""
    SHFE_FTDC_SPI_AccountIDMinLength = 50
    """投资者帐号代码最小长度"""
    SHFE_FTDC_SPI_UserRightLogon = 51
    """投资者开户默认登录权限"""
    SHFE_FTDC_SPI_SettlementBillTrade = 52
    """投资者交易结算单成交汇总方式"""
    SHFE_FTDC_SPI_TradingCode = 53
    """统一开户更新交易编码方式"""
    SHFE_FTDC_SPI_CheckFund = 54
    """结算是否判断存在未复核的出入金和分项资金"""
    SHFE_FTDC_SPI_CommModelRight = 55
    """是否启用手续费模板数据权限"""
    SHFE_FTDC_SPI_MarginModelRight = 57
    """是否启用保证金率模板数据权限"""
    SHFE_FTDC_SPI_IsStandardActive = 56
    """是否规范用户才能激活"""
    SHFE_FTDC_SPI_UploadSettlementFile = 85
    """上传的交易所结算文件路径"""
    SHFE_FTDC_SPI_DownloadCSRCFile = 68
    """上报保证金监控中心文件路径"""
    SHFE_FTDC_SPI_SettlementBillFile = 83
    """生成的结算单文件路径"""
    SHFE_FTDC_SPI_CSRCOthersFile = 67
    """证监会文件标识"""
    SHFE_FTDC_SPI_InvestorPhoto = 80
    """投资者照片路径"""
    SHFE_FTDC_SPI_CSRCData = 82
    """全结经纪公司上传文件路径"""
    SHFE_FTDC_SPI_InvestorPwdModel = 73
    """开户密码录入方式"""
    SHFE_FTDC_SPI_CFFEXInvestorSettleFile = 70
    """投资者中金所结算文件下载路径"""
    SHFE_FTDC_SPI_InvestorIDType = 97
    """投资者代码编码方式"""
    SHFE_FTDC_SPI_FreezeMaxReMain = 114
    """休眠户最高权益"""
    SHFE_FTDC_SPI_IsSync = 65
    """手续费相关操作实时上场开关"""
    SHFE_FTDC_SPI_RelieveOpenLimit = 79
    """解除开仓权限限制"""
    SHFE_FTDC_SPI_IsStandardFreeze = 88
    """是否规范用户才能休眠"""
    SHFE_FTDC_SPI_CZCENormalProductHedge = 66
    """郑商所是否开放所有品种套保交易"""
    SHFE_FTDC_SPI_NULL = 0


class TShfeFtdcTradeParamIDType(Enum):
    """交易系统参数代码类型"""
    SHFE_FTDC_TPID_EncryptionStandard = 69
    """系统加密算法"""
    SHFE_FTDC_TPID_RiskMode = 82
    """系统风险算法"""
    SHFE_FTDC_TPID_RiskModeGlobal = 71
    """系统风险算法是否全局 0-否 1-是"""
    SHFE_FTDC_TPID_modeEncode = 80
    """密码加密算法"""
    SHFE_FTDC_TPID_tickMode = 84
    """价格小数位数参数"""
    SHFE_FTDC_TPID_SingleUserSessionMaxNum = 83
    """用户最大会话数"""
    SHFE_FTDC_TPID_LoginFailMaxNum = 76
    """最大连续登录失败数"""
    SHFE_FTDC_TPID_IsAuthForce = 65
    """是否强制认证"""
    SHFE_FTDC_TPID_IsPosiFreeze = 70
    """是否冻结证券持仓"""
    SHFE_FTDC_TPID_IsPosiLimit = 77
    """是否限仓"""
    SHFE_FTDC_TPID_ForQuoteTimeInterval = 81
    """郑商所询价时间间隔"""
    SHFE_FTDC_TPID_IsFuturePosiLimit = 66
    """是否期货限仓"""
    SHFE_FTDC_TPID_IsFutureOrderFreq = 67
    """是否期货下单频率限制"""
    SHFE_FTDC_TPID_IsExecOrderProfit = 72
    """行权冻结是否计算盈利"""
    SHFE_FTDC_TPID_IsCheckBankAcc = 73
    """银期开户是否验证开户银行卡号是否是预留银行账户"""
    SHFE_FTDC_TPID_PasswordDeadLine = 74
    """弱密码最后修改日期"""
    SHFE_FTDC_TPID_IsStrongPassword = 75
    """强密码校验"""
    SHFE_FTDC_TPID_BalanceMorgage = 97
    """自有资金质押比"""
    SHFE_FTDC_TPID_MinPwdLen = 79
    """最小密码长度"""
    SHFE_FTDC_TPID_LoginFailMaxNumForIP = 85
    """IP当日最大登陆失败次数"""
    SHFE_FTDC_TPID_PasswordPeriod = 86
    """密码有效期"""
    SHFE_FTDC_TPID_NULL = 0


class TShfeFtdcFileIDType(Enum):
    """文件标识类型"""
    SHFE_FTDC_FI_SettlementFund = 70
    """资金数据"""
    SHFE_FTDC_FI_Trade = 84
    """成交数据"""
    SHFE_FTDC_FI_InvestorPosition = 80
    """投资者持仓数据"""
    SHFE_FTDC_FI_SubEntryFund = 79
    """投资者分项资金数据"""
    SHFE_FTDC_FI_CZCECombinationPos = 67
    """组合持仓数据"""
    SHFE_FTDC_FI_CSRCData = 82
    """上报保证金监控中心数据"""
    SHFE_FTDC_FI_CZCEClose = 76
    """郑商所平仓了结数据"""
    SHFE_FTDC_FI_CZCENoClose = 78
    """郑商所非平仓了结数据"""
    SHFE_FTDC_FI_PositionDtl = 68
    """持仓明细数据"""
    SHFE_FTDC_FI_OptionStrike = 83
    """期权执行文件"""
    SHFE_FTDC_FI_SettlementPriceComparison = 77
    """结算价比对文件"""
    SHFE_FTDC_FI_NonTradePosChange = 66
    """上期所非持仓变动明细"""
    SHFE_FTDC_FI_NULL = 0


class TShfeFtdcFileTypeType(Enum):
    """文件上传类型类型"""
    SHFE_FTDC_FUT_Settlement = 48
    """结算"""
    SHFE_FTDC_FUT_Check = 49
    """核对"""
    SHFE_FTDC_FUT_NULL = 0


class TShfeFtdcFileFormatType(Enum):
    """文件格式类型"""
    SHFE_FTDC_FFT_Txt = 48
    """文本文件(.txt)"""
    SHFE_FTDC_FFT_Zip = 49
    """压缩文件(.zip)"""
    SHFE_FTDC_FFT_DBF = 50
    """DBF文件(.dbf)"""
    SHFE_FTDC_FFT_NULL = 0


class TShfeFtdcFileUploadStatusType(Enum):
    """文件状态类型"""
    SHFE_FTDC_FUS_SucceedUpload = 49
    """上传成功"""
    SHFE_FTDC_FUS_FailedUpload = 50
    """上传失败"""
    SHFE_FTDC_FUS_SucceedLoad = 51
    """导入成功"""
    SHFE_FTDC_FUS_PartSucceedLoad = 52
    """导入部分成功"""
    SHFE_FTDC_FUS_FailedLoad = 53
    """导入失败"""
    SHFE_FTDC_FUS_NULL = 0


class TShfeFtdcTransferDirectionType(Enum):
    """移仓方向类型"""
    SHFE_FTDC_TD_Out = 48
    """移出"""
    SHFE_FTDC_TD_In = 49
    """移入"""
    SHFE_FTDC_TD_NULL = 0


class TShfeFtdcSpecialCreateRuleType(Enum):
    """特殊的创建规则类型"""
    SHFE_FTDC_SC_NoSpecialRule = 48
    """没有特殊创建规则"""
    SHFE_FTDC_SC_NoSpringFestival = 49
    """不包含春节"""
    SHFE_FTDC_SC_NULL = 0


class TShfeFtdcBasisPriceTypeType(Enum):
    """挂牌基准价类型类型"""
    SHFE_FTDC_IPT_LastSettlement = 49
    """上一合约结算价"""
    SHFE_FTDC_IPT_LaseClose = 50
    """上一合约收盘价"""
    SHFE_FTDC_IPT_NULL = 0


class TShfeFtdcProductLifePhaseType(Enum):
    """产品生命周期状态类型"""
    SHFE_FTDC_PLP_Active = 49
    """活跃"""
    SHFE_FTDC_PLP_NonActive = 50
    """不活跃"""
    SHFE_FTDC_PLP_Canceled = 51
    """注销"""
    SHFE_FTDC_PLP_NULL = 0


class TShfeFtdcDeliveryModeType(Enum):
    """交割方式类型"""
    SHFE_FTDC_DM_CashDeliv = 49
    """现金交割"""
    SHFE_FTDC_DM_CommodityDeliv = 50
    """实物交割"""
    SHFE_FTDC_DM_NULL = 0


class TShfeFtdcFundIOTypeType(Enum):
    """出入金类型类型"""
    SHFE_FTDC_FIOT_FundIO = 49
    """出入金"""
    SHFE_FTDC_FIOT_Transfer = 50
    """银期转帐"""
    SHFE_FTDC_FIOT_SwapCurrency = 51
    """银期换汇"""
    SHFE_FTDC_FIOT_NULL = 0


class TShfeFtdcFundTypeType(Enum):
    """资金类型类型"""
    SHFE_FTDC_FT_Deposite = 49
    """银行存款"""
    SHFE_FTDC_FT_ItemFund = 50
    """分项资金"""
    SHFE_FTDC_FT_Company = 51
    """公司调整"""
    SHFE_FTDC_FT_InnerTransfer = 52
    """资金内转"""
    SHFE_FTDC_FT_NULL = 0


class TShfeFtdcFundDirectionType(Enum):
    """出入金方向类型"""
    SHFE_FTDC_FD_In = 49
    """入金"""
    SHFE_FTDC_FD_Out = 50
    """出金"""
    SHFE_FTDC_FD_NULL = 0


class TShfeFtdcFundStatusType(Enum):
    """资金状态类型"""
    SHFE_FTDC_FS_Record = 49
    """已录入"""
    SHFE_FTDC_FS_Check = 50
    """已复核"""
    SHFE_FTDC_FS_Charge = 51
    """已冲销"""
    SHFE_FTDC_FS_NULL = 0


class TShfeFtdcPublishStatusType(Enum):
    """发布状态类型"""
    SHFE_FTDC_PS_None = 49
    """未发布"""
    SHFE_FTDC_PS_Publishing = 50
    """正在发布"""
    SHFE_FTDC_PS_Published = 51
    """已发布"""
    SHFE_FTDC_PS_NULL = 0


class TShfeFtdcSystemStatusType(Enum):
    """系统状态类型"""
    SHFE_FTDC_ES_NonActive = 49
    """不活跃"""
    SHFE_FTDC_ES_Startup = 50
    """启动"""
    SHFE_FTDC_ES_Initialize = 51
    """交易开始初始化"""
    SHFE_FTDC_ES_Initialized = 52
    """交易完成初始化"""
    SHFE_FTDC_ES_Close = 53
    """收市开始"""
    SHFE_FTDC_ES_Closed = 54
    """收市完成"""
    SHFE_FTDC_ES_Settlement = 55
    """结算"""
    SHFE_FTDC_ES_NULL = 0


class TShfeFtdcSettlementStatusType(Enum):
    """结算状态类型"""
    SHFE_FTDC_STS_Initialize = 48
    """初始"""
    SHFE_FTDC_STS_Settlementing = 49
    """结算中"""
    SHFE_FTDC_STS_Settlemented = 50
    """已结算"""
    SHFE_FTDC_STS_Finished = 51
    """结算完成"""
    SHFE_FTDC_STS_NULL = 0


class TShfeFtdcInvestorTypeType(Enum):
    """投资者类型类型"""
    SHFE_FTDC_CT_Person = 48
    """自然人"""
    SHFE_FTDC_CT_Company = 49
    """法人"""
    SHFE_FTDC_CT_Fund = 50
    """投资基金"""
    SHFE_FTDC_CT_SpecialOrgan = 51
    """特殊法人"""
    SHFE_FTDC_CT_Asset = 52
    """资管户"""
    SHFE_FTDC_CT_NULL = 0


class TShfeFtdcBrokerTypeType(Enum):
    """经纪公司类型类型"""
    SHFE_FTDC_BT_Trade = 48
    """交易会员"""
    SHFE_FTDC_BT_TradeSettle = 49
    """交易结算会员"""
    SHFE_FTDC_BT_NULL = 0


class TShfeFtdcRiskLevelType(Enum):
    """风险等级类型"""
    SHFE_FTDC_FAS_Low = 49
    """低风险客户"""
    SHFE_FTDC_FAS_Normal = 50
    """普通客户"""
    SHFE_FTDC_FAS_Focus = 51
    """关注客户"""
    SHFE_FTDC_FAS_Risk = 52
    """风险客户"""
    SHFE_FTDC_FAS_NULL = 0


class TShfeFtdcFeeAcceptStyleType(Enum):
    """手续费收取方式类型"""
    SHFE_FTDC_FAS_ByTrade = 49
    """按交易收取"""
    SHFE_FTDC_FAS_ByDeliv = 50
    """按交割收取"""
    SHFE_FTDC_FAS_None = 51
    """不收"""
    SHFE_FTDC_FAS_FixFee = 52
    """按指定手续费收取"""
    SHFE_FTDC_FAS_NULL = 0


class TShfeFtdcPasswordTypeType(Enum):
    """密码类型类型"""
    SHFE_FTDC_PWDT_Trade = 49
    """交易密码"""
    SHFE_FTDC_PWDT_Account = 50
    """资金密码"""
    SHFE_FTDC_PWDT_NULL = 0


class TShfeFtdcAlgorithmType(Enum):
    """盈亏算法类型"""
    SHFE_FTDC_AG_All = 49
    """浮盈浮亏都计算"""
    SHFE_FTDC_AG_OnlyLost = 50
    """浮盈不计，浮亏计"""
    SHFE_FTDC_AG_OnlyGain = 51
    """浮盈计，浮亏不计"""
    SHFE_FTDC_AG_None = 52
    """浮盈浮亏都不计算"""
    SHFE_FTDC_AG_NULL = 0


class TShfeFtdcIncludeCloseProfitType(Enum):
    """是否包含平仓盈利类型"""
    SHFE_FTDC_ICP_Include = 48
    """包含平仓盈利"""
    SHFE_FTDC_ICP_NotInclude = 50
    """不包含平仓盈利"""
    SHFE_FTDC_ICP_NULL = 0


class TShfeFtdcAllWithoutTradeType(Enum):
    """是否受可提比例限制类型"""
    SHFE_FTDC_AWT_Enable = 48
    """无仓无成交不受可提比例限制"""
    SHFE_FTDC_AWT_Disable = 50
    """受可提比例限制"""
    SHFE_FTDC_AWT_NoHoldEnable = 51
    """无仓不受可提比例限制"""
    SHFE_FTDC_AWT_NULL = 0


class TShfeFtdcFuturePwdFlagType(Enum):
    """资金密码核对标志类型"""
    SHFE_FTDC_FPWD_UnCheck = 48
    """不核对"""
    SHFE_FTDC_FPWD_Check = 49
    """核对"""
    SHFE_FTDC_FPWD_NULL = 0


class TShfeFtdcTransferTypeType(Enum):
    """银期转账类型类型"""
    SHFE_FTDC_TT_BankToFuture = 48
    """银行转期货"""
    SHFE_FTDC_TT_FutureToBank = 49
    """期货转银行"""
    SHFE_FTDC_TT_NULL = 0


class TShfeFtdcTransferValidFlagType(Enum):
    """转账有效标志类型"""
    SHFE_FTDC_TVF_Invalid = 48
    """无效或失败"""
    SHFE_FTDC_TVF_Valid = 49
    """有效"""
    SHFE_FTDC_TVF_Reverse = 50
    """冲正"""
    SHFE_FTDC_TVF_NULL = 0


class TShfeFtdcReasonType(Enum):
    """事由类型"""
    SHFE_FTDC_RN_CD = 48
    """错单"""
    SHFE_FTDC_RN_ZT = 49
    """资金在途"""
    SHFE_FTDC_RN_QT = 50
    """其它"""
    SHFE_FTDC_RN_NULL = 0


class TShfeFtdcSexType(Enum):
    """性别类型"""
    SHFE_FTDC_SEX_None = 48
    """未知"""
    SHFE_FTDC_SEX_Man = 49
    """男"""
    SHFE_FTDC_SEX_Woman = 50
    """女"""
    SHFE_FTDC_SEX_NULL = 0


class TShfeFtdcUserTypeType(Enum):
    """用户类型类型"""
    SHFE_FTDC_UT_Investor = 48
    """投资者"""
    SHFE_FTDC_UT_Operator = 49
    """操作员"""
    SHFE_FTDC_UT_SuperUser = 50
    """管理员"""
    SHFE_FTDC_UT_NULL = 0


class TShfeFtdcRateTypeType(Enum):
    """费率类型类型"""
    SHFE_FTDC_RATETYPE_MarginRate = 50
    """保证金率"""
    SHFE_FTDC_RATETYPE_NULL = 0


class TShfeFtdcNoteTypeType(Enum):
    """通知类型类型"""
    SHFE_FTDC_NOTETYPE_TradeSettleBill = 49
    """交易结算单"""
    SHFE_FTDC_NOTETYPE_TradeSettleMonth = 50
    """交易结算月报"""
    SHFE_FTDC_NOTETYPE_CallMarginNotes = 51
    """追加保证金通知书"""
    SHFE_FTDC_NOTETYPE_ForceCloseNotes = 52
    """强行平仓通知书"""
    SHFE_FTDC_NOTETYPE_TradeNotes = 53
    """成交通知书"""
    SHFE_FTDC_NOTETYPE_DelivNotes = 54
    """交割通知书"""
    SHFE_FTDC_NOTETYPE_NULL = 0


class TShfeFtdcSettlementStyleType(Enum):
    """结算单方式类型"""
    SHFE_FTDC_SBS_Day = 49
    """逐日盯市"""
    SHFE_FTDC_SBS_Volume = 50
    """逐笔对冲"""
    SHFE_FTDC_SBS_NULL = 0


class TShfeFtdcSettlementBillTypeType(Enum):
    """结算单类型类型"""
    SHFE_FTDC_ST_Day = 48
    """日报"""
    SHFE_FTDC_ST_Month = 49
    """月报"""
    SHFE_FTDC_ST_NULL = 0


class TShfeFtdcUserRightTypeType(Enum):
    """客户权限类型类型"""
    SHFE_FTDC_URT_Logon = 49
    """登录"""
    SHFE_FTDC_URT_Transfer = 50
    """银期转帐"""
    SHFE_FTDC_URT_EMail = 51
    """邮寄结算单"""
    SHFE_FTDC_URT_Fax = 52
    """传真结算单"""
    SHFE_FTDC_URT_ConditionOrder = 53
    """条件单"""
    SHFE_FTDC_URT_NULL = 0


class TShfeFtdcMarginPriceTypeType(Enum):
    """保证金价格类型类型"""
    SHFE_FTDC_MPT_PreSettlementPrice = 49
    """昨结算价"""
    SHFE_FTDC_MPT_SettlementPrice = 50
    """最新价"""
    SHFE_FTDC_MPT_AveragePrice = 51
    """成交均价"""
    SHFE_FTDC_MPT_OpenPrice = 52
    """开仓价"""
    SHFE_FTDC_MPT_NULL = 0


class TShfeFtdcBillGenStatusType(Enum):
    """结算单生成状态类型"""
    SHFE_FTDC_BGS_None = 48
    """未生成"""
    SHFE_FTDC_BGS_NoGenerated = 49
    """生成中"""
    SHFE_FTDC_BGS_Generated = 50
    """已生成"""
    SHFE_FTDC_BGS_NULL = 0


class TShfeFtdcAlgoTypeType(Enum):
    """算法类型类型"""
    SHFE_FTDC_AT_HandlePositionAlgo = 49
    """持仓处理算法"""
    SHFE_FTDC_AT_FindMarginRateAlgo = 50
    """寻找保证金率算法"""
    SHFE_FTDC_AT_NULL = 0


class TShfeFtdcHandlePositionAlgoIDType(Enum):
    """持仓处理算法编号类型"""
    SHFE_FTDC_HPA_Base = 49
    """基本"""
    SHFE_FTDC_HPA_DCE = 50
    """大连商品交易所"""
    SHFE_FTDC_HPA_CZCE = 51
    """郑州商品交易所"""
    SHFE_FTDC_HPA_NULL = 0


class TShfeFtdcFindMarginRateAlgoIDType(Enum):
    """寻找保证金率算法编号类型"""
    SHFE_FTDC_FMRA_Base = 49
    """基本"""
    SHFE_FTDC_FMRA_DCE = 50
    """大连商品交易所"""
    SHFE_FTDC_FMRA_CZCE = 51
    """郑州商品交易所"""
    SHFE_FTDC_FMRA_NULL = 0


class TShfeFtdcHandleTradingAccountAlgoIDType(Enum):
    """资金处理算法编号类型"""
    SHFE_FTDC_HTAA_Base = 49
    """基本"""
    SHFE_FTDC_HTAA_DCE = 50
    """大连商品交易所"""
    SHFE_FTDC_HTAA_CZCE = 51
    """郑州商品交易所"""
    SHFE_FTDC_HTAA_NULL = 0


class TShfeFtdcPersonTypeType(Enum):
    """联系人类型类型"""
    SHFE_FTDC_PST_Order = 49
    """指定下单人"""
    SHFE_FTDC_PST_Open = 50
    """开户授权人"""
    SHFE_FTDC_PST_Fund = 51
    """资金调拨人"""
    SHFE_FTDC_PST_Settlement = 52
    """结算单确认人"""
    SHFE_FTDC_PST_Company = 53
    """法人"""
    SHFE_FTDC_PST_Corporation = 54
    """法人代表"""
    SHFE_FTDC_PST_LinkMan = 55
    """投资者联系人"""
    SHFE_FTDC_PST_Ledger = 56
    """分户管理资产负责人"""
    SHFE_FTDC_PST_Trustee = 57
    """托（保）管人"""
    SHFE_FTDC_PST_TrusteeCorporation = 65
    """托（保）管机构法人代表"""
    SHFE_FTDC_PST_TrusteeOpen = 66
    """托（保）管机构开户授权人"""
    SHFE_FTDC_PST_TrusteeContact = 67
    """托（保）管机构联系人"""
    SHFE_FTDC_PST_ForeignerRefer = 68
    """境外自然人参考证件"""
    SHFE_FTDC_PST_CorporationRefer = 69
    """法人代表参考证件"""
    SHFE_FTDC_PST_NULL = 0


class TShfeFtdcQueryInvestorRangeType(Enum):
    """查询范围类型"""
    SHFE_FTDC_QIR_All = 49
    """所有"""
    SHFE_FTDC_QIR_Group = 50
    """查询分类"""
    SHFE_FTDC_QIR_Single = 51
    """单一投资者"""
    SHFE_FTDC_QIR_NULL = 0


class TShfeFtdcInvestorRiskStatusType(Enum):
    """投资者风险状态类型"""
    SHFE_FTDC_IRS_Normal = 49
    """正常"""
    SHFE_FTDC_IRS_Warn = 50
    """警告"""
    SHFE_FTDC_IRS_Call = 51
    """追保"""
    SHFE_FTDC_IRS_Force = 52
    """强平"""
    SHFE_FTDC_IRS_Exception = 53
    """异常"""
    SHFE_FTDC_IRS_NULL = 0


class TShfeFtdcUserEventTypeType(Enum):
    """用户事件类型类型"""
    SHFE_FTDC_UET_Login = 49
    """登录"""
    SHFE_FTDC_UET_Logout = 50
    """登出"""
    SHFE_FTDC_UET_Trading = 51
    """交易成功"""
    SHFE_FTDC_UET_TradingError = 52
    """交易失败"""
    SHFE_FTDC_UET_UpdatePassword = 53
    """修改密码"""
    SHFE_FTDC_UET_Authenticate = 54
    """客户端认证"""
    SHFE_FTDC_UET_Other = 57
    """其他"""
    SHFE_FTDC_UET_NULL = 0


class TShfeFtdcCloseStyleType(Enum):
    """平仓方式类型"""
    SHFE_FTDC_ICS_Close = 48
    """先开先平"""
    SHFE_FTDC_ICS_CloseToday = 49
    """先平今再平昨"""
    SHFE_FTDC_ICS_NULL = 0


class TShfeFtdcStatModeType(Enum):
    """统计方式类型"""
    SHFE_FTDC_SM_Non = 48
    """----"""
    SHFE_FTDC_SM_Instrument = 49
    """按合约统计"""
    SHFE_FTDC_SM_Product = 50
    """按产品统计"""
    SHFE_FTDC_SM_Investor = 51
    """按投资者统计"""
    SHFE_FTDC_SM_NULL = 0


class TShfeFtdcParkedOrderStatusType(Enum):
    """预埋单状态类型"""
    SHFE_FTDC_PAOS_NotSend = 49
    """未发送"""
    SHFE_FTDC_PAOS_Send = 50
    """已发送"""
    SHFE_FTDC_PAOS_Deleted = 51
    """已删除"""
    SHFE_FTDC_PAOS_NULL = 0


class TShfeFtdcVirDealStatusType(Enum):
    """处理状态类型"""
    SHFE_FTDC_VDS_Dealing = 49
    """正在处理"""
    SHFE_FTDC_VDS_DeaclSucceed = 50
    """处理成功"""
    SHFE_FTDC_VDS_NULL = 0


class TShfeFtdcOrgSystemIDType(Enum):
    """原有系统代码类型"""
    SHFE_FTDC_ORGS_Standard = 48
    """综合交易平台"""
    SHFE_FTDC_ORGS_ESunny = 49
    """易盛系统"""
    SHFE_FTDC_ORGS_KingStarV6 = 50
    """金仕达V6系统"""
    SHFE_FTDC_ORGS_NULL = 0


class TShfeFtdcVirTradeStatusType(Enum):
    """交易状态类型"""
    SHFE_FTDC_VTS_NaturalDeal = 48
    """正常处理中"""
    SHFE_FTDC_VTS_SucceedEnd = 49
    """成功结束"""
    SHFE_FTDC_VTS_FailedEND = 50
    """失败结束"""
    SHFE_FTDC_VTS_Exception = 51
    """异常中"""
    SHFE_FTDC_VTS_ManualDeal = 52
    """已人工异常处理"""
    SHFE_FTDC_VTS_MesException = 53
    """通讯异常 ，请人工处理"""
    SHFE_FTDC_VTS_SysException = 54
    """系统出错，请人工处理"""
    SHFE_FTDC_VTS_NULL = 0


class TShfeFtdcVirBankAccTypeType(Enum):
    """银行帐户类型类型"""
    SHFE_FTDC_VBAT_BankBook = 49
    """存折"""
    SHFE_FTDC_VBAT_BankCard = 50
    """储蓄卡"""
    SHFE_FTDC_VBAT_CreditCard = 51
    """信用卡"""
    SHFE_FTDC_VBAT_NULL = 0


class TShfeFtdcVirementStatusType(Enum):
    """银行帐户类型类型"""
    SHFE_FTDC_VMS_Natural = 48
    """正常"""
    SHFE_FTDC_VMS_Canceled = 57
    """销户"""
    SHFE_FTDC_VMS_NULL = 0


class TShfeFtdcVirementAvailAbilityType(Enum):
    """有效标志类型"""
    SHFE_FTDC_VAA_NoAvailAbility = 48
    """未确认"""
    SHFE_FTDC_VAA_AvailAbility = 49
    """有效"""
    SHFE_FTDC_VAA_Repeal = 50
    """冲正"""
    SHFE_FTDC_VAA_NULL = 0


class TShfeFtdcVirementTradeCodeType(Enum):
    """交易代码类型"""
    SHFE_FTDC_VTC_BankBankToFuture = 49
    """银行发起银行资金转期货"""
    SHFE_FTDC_VTC_BankFutureToBank = 50
    """银行发起期货资金转银行"""
    SHFE_FTDC_VTC_FutureBankToFuture = 49
    """期货发起银行资金转期货"""
    SHFE_FTDC_VTC_FutureFutureToBank = 50
    """期货发起期货资金转银行"""
    SHFE_FTDC_VTC_NULL = 0


class TShfeFtdcAMLGenStatusType(Enum):
    """Aml生成方式类型"""
    SHFE_FTDC_GEN_Program = 48
    """程序生成"""
    SHFE_FTDC_GEN_HandWork = 49
    """人工生成"""
    SHFE_FTDC_GEN_NULL = 0


class TShfeFtdcCFMMCKeyKindType(Enum):
    """动态密钥类别(保证金监管)类型"""
    SHFE_FTDC_CFMMCKK_REQUEST = 82
    """主动请求更新"""
    SHFE_FTDC_CFMMCKK_AUTO = 65
    """CFMMC自动更新"""
    SHFE_FTDC_CFMMCKK_MANUAL = 77
    """CFMMC手动更新"""
    SHFE_FTDC_CFMMCKK_NULL = 0


class TShfeFtdcCertificationTypeType(Enum):
    """证件类型类型"""
    SHFE_FTDC_CFT_IDCard = 48
    """身份证"""
    SHFE_FTDC_CFT_Passport = 49
    """护照"""
    SHFE_FTDC_CFT_OfficerIDCard = 50
    """军官证"""
    SHFE_FTDC_CFT_SoldierIDCard = 51
    """士兵证"""
    SHFE_FTDC_CFT_HomeComingCard = 52
    """回乡证"""
    SHFE_FTDC_CFT_HouseholdRegister = 53
    """户口簿"""
    SHFE_FTDC_CFT_LicenseNo = 54
    """营业执照号"""
    SHFE_FTDC_CFT_InstitutionCodeCard = 55
    """组织机构代码证"""
    SHFE_FTDC_CFT_TempLicenseNo = 56
    """临时营业执照号"""
    SHFE_FTDC_CFT_NoEnterpriseLicenseNo = 57
    """民办非企业登记证书"""
    SHFE_FTDC_CFT_OtherCard = 120
    """其他证件"""
    SHFE_FTDC_CFT_SuperDepAgree = 97
    """主管部门批文"""
    SHFE_FTDC_CFT_NULL = 0


class TShfeFtdcFileBusinessCodeType(Enum):
    """文件业务功能类型"""
    SHFE_FTDC_FBC_Others = 48
    """其他"""
    SHFE_FTDC_FBC_TransferDetails = 49
    """转账交易明细对账"""
    SHFE_FTDC_FBC_CustAccStatus = 50
    """客户账户状态对账"""
    SHFE_FTDC_FBC_AccountTradeDetails = 51
    """账户类交易明细对账"""
    SHFE_FTDC_FBC_FutureAccountChangeInfoDetails = 52
    """期货账户信息变更明细对账"""
    SHFE_FTDC_FBC_CustMoneyDetail = 53
    """客户资金台账余额明细对账"""
    SHFE_FTDC_FBC_CustCancelAccountInfo = 54
    """客户销户结息明细对账"""
    SHFE_FTDC_FBC_CustMoneyResult = 55
    """客户资金余额对账结果"""
    SHFE_FTDC_FBC_OthersExceptionResult = 56
    """其它对账异常结果文件"""
    SHFE_FTDC_FBC_CustInterestNetMoneyDetails = 57
    """客户结息净额明细"""
    SHFE_FTDC_FBC_CustMoneySendAndReceiveDetails = 97
    """客户资金交收明细"""
    SHFE_FTDC_FBC_CorporationMoneyTotal = 98
    """法人存管银行资金交收汇总"""
    SHFE_FTDC_FBC_MainbodyMoneyTotal = 99
    """主体间资金交收汇总"""
    SHFE_FTDC_FBC_MainPartMonitorData = 100
    """总分平衡监管数据"""
    SHFE_FTDC_FBC_PreparationMoney = 101
    """存管银行备付金余额"""
    SHFE_FTDC_FBC_BankMoneyMonitorData = 102
    """协办存管银行资金监管数据"""
    SHFE_FTDC_FBC_NULL = 0


class TShfeFtdcCashExchangeCodeType(Enum):
    """汇钞标志类型"""
    SHFE_FTDC_CEC_Exchange = 49
    """汇"""
    SHFE_FTDC_CEC_Cash = 50
    """钞"""
    SHFE_FTDC_CEC_NULL = 0


class TShfeFtdcYesNoIndicatorType(Enum):
    """是或否标识类型"""
    SHFE_FTDC_YNI_Yes = 48
    """是"""
    SHFE_FTDC_YNI_No = 49
    """否"""
    SHFE_FTDC_YNI_NULL = 0


class TShfeFtdcBanlanceTypeType(Enum):
    """余额类型类型"""
    SHFE_FTDC_BLT_CurrentMoney = 48
    """当前余额"""
    SHFE_FTDC_BLT_UsableMoney = 49
    """可用余额"""
    SHFE_FTDC_BLT_FetchableMoney = 50
    """可取余额"""
    SHFE_FTDC_BLT_FreezeMoney = 51
    """冻结余额"""
    SHFE_FTDC_BLT_NULL = 0


class TShfeFtdcGenderType(Enum):
    """性别类型"""
    SHFE_FTDC_GD_Unknown = 48
    """未知状态"""
    SHFE_FTDC_GD_Male = 49
    """男"""
    SHFE_FTDC_GD_Female = 50
    """女"""
    SHFE_FTDC_GD_NULL = 0


class TShfeFtdcFeePayFlagType(Enum):
    """费用支付标志类型"""
    SHFE_FTDC_FPF_BEN = 48
    """由受益方支付费用"""
    SHFE_FTDC_FPF_OUR = 49
    """由发送方支付费用"""
    SHFE_FTDC_FPF_SHA = 50
    """由发送方支付发起的费用，受益方支付接受的费用"""
    SHFE_FTDC_FPF_NULL = 0


class TShfeFtdcPassWordKeyTypeType(Enum):
    """密钥类型类型"""
    SHFE_FTDC_PWKT_ExchangeKey = 48
    """交换密钥"""
    SHFE_FTDC_PWKT_PassWordKey = 49
    """密码密钥"""
    SHFE_FTDC_PWKT_MACKey = 50
    """MAC密钥"""
    SHFE_FTDC_PWKT_MessageKey = 51
    """报文密钥"""
    SHFE_FTDC_PWKT_NULL = 0


class TShfeFtdcFBTPassWordTypeType(Enum):
    """密码类型类型"""
    SHFE_FTDC_PWT_Query = 48
    """查询"""
    SHFE_FTDC_PWT_Fetch = 49
    """取款"""
    SHFE_FTDC_PWT_Transfer = 50
    """转帐"""
    SHFE_FTDC_PWT_Trade = 51
    """交易"""
    SHFE_FTDC_PWT_NULL = 0


class TShfeFtdcFBTEncryModeType(Enum):
    """加密方式类型"""
    SHFE_FTDC_EM_NoEncry = 48
    """不加密"""
    SHFE_FTDC_EM_DES = 49
    """DES"""
    SHFE_FTDC_EM_3DES = 50
    """3DES"""
    SHFE_FTDC_EM_NULL = 0


class TShfeFtdcBankRepealFlagType(Enum):
    """银行冲正标志类型"""
    SHFE_FTDC_BRF_BankNotNeedRepeal = 48
    """银行无需自动冲正"""
    SHFE_FTDC_BRF_BankWaitingRepeal = 49
    """银行待自动冲正"""
    SHFE_FTDC_BRF_BankBeenRepealed = 50
    """银行已自动冲正"""
    SHFE_FTDC_BRF_NULL = 0


class TShfeFtdcBrokerRepealFlagType(Enum):
    """期商冲正标志类型"""
    SHFE_FTDC_BRORF_BrokerNotNeedRepeal = 48
    """期商无需自动冲正"""
    SHFE_FTDC_BRORF_BrokerWaitingRepeal = 49
    """期商待自动冲正"""
    SHFE_FTDC_BRORF_BrokerBeenRepealed = 50
    """期商已自动冲正"""
    SHFE_FTDC_BRORF_NULL = 0


class TShfeFtdcInstitutionTypeType(Enum):
    """机构类别类型"""
    SHFE_FTDC_TS_Bank = 48
    """银行"""
    SHFE_FTDC_TS_Future = 49
    """期商"""
    SHFE_FTDC_TS_Store = 50
    """券商"""
    SHFE_FTDC_TS_NULL = 0


class TShfeFtdcLastFragmentType(Enum):
    """最后分片标志类型"""
    SHFE_FTDC_LF_Yes = 48
    """是最后分片"""
    SHFE_FTDC_LF_No = 49
    """不是最后分片"""
    SHFE_FTDC_LF_NULL = 0


class TShfeFtdcBankAccStatusType(Enum):
    """银行账户状态类型"""
    SHFE_FTDC_BAS_Normal = 48
    """正常"""
    SHFE_FTDC_BAS_Freeze = 49
    """冻结"""
    SHFE_FTDC_BAS_ReportLoss = 50
    """挂失"""
    SHFE_FTDC_BAS_NULL = 0


class TShfeFtdcMoneyAccountStatusType(Enum):
    """资金账户状态类型"""
    SHFE_FTDC_MAS_Normal = 48
    """正常"""
    SHFE_FTDC_MAS_Cancel = 49
    """销户"""
    SHFE_FTDC_MAS_NULL = 0


class TShfeFtdcManageStatusType(Enum):
    """存管状态类型"""
    SHFE_FTDC_MSS_Point = 48
    """指定存管"""
    SHFE_FTDC_MSS_PrePoint = 49
    """预指定"""
    SHFE_FTDC_MSS_CancelPoint = 50
    """撤销指定"""
    SHFE_FTDC_MSS_NULL = 0


class TShfeFtdcSystemTypeType(Enum):
    """应用系统类型类型"""
    SHFE_FTDC_SYT_FutureBankTransfer = 48
    """银期转帐"""
    SHFE_FTDC_SYT_StockBankTransfer = 49
    """银证转帐"""
    SHFE_FTDC_SYT_TheThirdPartStore = 50
    """第三方存管"""
    SHFE_FTDC_SYT_NULL = 0


class TShfeFtdcTxnEndFlagType(Enum):
    """银期转帐划转结果标志类型"""
    SHFE_FTDC_TEF_NormalProcessing = 48
    """正常处理中"""
    SHFE_FTDC_TEF_Success = 49
    """成功结束"""
    SHFE_FTDC_TEF_Failed = 50
    """失败结束"""
    SHFE_FTDC_TEF_Abnormal = 51
    """异常中"""
    SHFE_FTDC_TEF_ManualProcessedForException = 52
    """已人工异常处理"""
    SHFE_FTDC_TEF_CommuFailedNeedManualProcess = 53
    """通讯异常 ，请人工处理"""
    SHFE_FTDC_TEF_SysErrorNeedManualProcess = 54
    """系统出错，请人工处理"""
    SHFE_FTDC_TEF_NULL = 0


class TShfeFtdcProcessStatusType(Enum):
    """银期转帐服务处理状态类型"""
    SHFE_FTDC_PSS_NotProcess = 48
    """未处理"""
    SHFE_FTDC_PSS_StartProcess = 49
    """开始处理"""
    SHFE_FTDC_PSS_Finished = 50
    """处理完成"""
    SHFE_FTDC_PSS_NULL = 0


class TShfeFtdcCustTypeType(Enum):
    """客户类型类型"""
    SHFE_FTDC_CUSTT_Person = 48
    """自然人"""
    SHFE_FTDC_CUSTT_Institution = 49
    """机构户"""
    SHFE_FTDC_CUSTT_NULL = 0


class TShfeFtdcFBTTransferDirectionType(Enum):
    """银期转帐方向类型"""
    SHFE_FTDC_FBTTD_FromBankToFuture = 49
    """入金，银行转期货"""
    SHFE_FTDC_FBTTD_FromFutureToBank = 50
    """出金，期货转银行"""
    SHFE_FTDC_FBTTD_NULL = 0


class TShfeFtdcOpenOrDestroyType(Enum):
    """开销户类别类型"""
    SHFE_FTDC_OOD_Open = 49
    """开户"""
    SHFE_FTDC_OOD_Destroy = 48
    """销户"""
    SHFE_FTDC_OOD_NULL = 0


class TShfeFtdcAvailabilityFlagType(Enum):
    """有效标志类型"""
    SHFE_FTDC_AVAF_Invalid = 48
    """未确认"""
    SHFE_FTDC_AVAF_Valid = 49
    """有效"""
    SHFE_FTDC_AVAF_Repeal = 50
    """冲正"""
    SHFE_FTDC_AVAF_NULL = 0


class TShfeFtdcOrganTypeType(Enum):
    """机构类型类型"""
    SHFE_FTDC_OT_Bank = 49
    """银行代理"""
    SHFE_FTDC_OT_Future = 50
    """交易前置"""
    SHFE_FTDC_OT_PlateForm = 57
    """银期转帐平台管理"""
    SHFE_FTDC_OT_NULL = 0


class TShfeFtdcOrganLevelType(Enum):
    """机构级别类型"""
    SHFE_FTDC_OL_HeadQuarters = 49
    """银行总行或期商总部"""
    SHFE_FTDC_OL_Branch = 50
    """银行分中心或期货公司营业部"""
    SHFE_FTDC_OL_NULL = 0


class TShfeFtdcProtocalIDType(Enum):
    """协议类型类型"""
    SHFE_FTDC_PID_FutureProtocal = 48
    """期商协议"""
    SHFE_FTDC_PID_ICBCProtocal = 49
    """工行协议"""
    SHFE_FTDC_PID_ABCProtocal = 50
    """农行协议"""
    SHFE_FTDC_PID_CBCProtocal = 51
    """中国银行协议"""
    SHFE_FTDC_PID_CCBProtocal = 52
    """建行协议"""
    SHFE_FTDC_PID_BOCOMProtocal = 53
    """交行协议"""
    SHFE_FTDC_PID_FBTPlateFormProtocal = 88
    """银期转帐平台协议"""
    SHFE_FTDC_PID_NULL = 0


class TShfeFtdcConnectModeType(Enum):
    """套接字连接方式类型"""
    SHFE_FTDC_CM_ShortConnect = 48
    """短连接"""
    SHFE_FTDC_CM_LongConnect = 49
    """长连接"""
    SHFE_FTDC_CM_NULL = 0


class TShfeFtdcSyncModeType(Enum):
    """套接字通信方式类型"""
    SHFE_FTDC_SRM_ASync = 48
    """异步"""
    SHFE_FTDC_SRM_Sync = 49
    """同步"""
    SHFE_FTDC_SRM_NULL = 0


class TShfeFtdcBankAccTypeType(Enum):
    """银行帐号类型类型"""
    SHFE_FTDC_BAT_BankBook = 49
    """银行存折"""
    SHFE_FTDC_BAT_SavingCard = 50
    """储蓄卡"""
    SHFE_FTDC_BAT_CreditCard = 51
    """信用卡"""
    SHFE_FTDC_BAT_NULL = 0


class TShfeFtdcFutureAccTypeType(Enum):
    """期货公司帐号类型类型"""
    SHFE_FTDC_FAT_BankBook = 49
    """银行存折"""
    SHFE_FTDC_FAT_SavingCard = 50
    """储蓄卡"""
    SHFE_FTDC_FAT_CreditCard = 51
    """信用卡"""
    SHFE_FTDC_FAT_NULL = 0


class TShfeFtdcOrganStatusType(Enum):
    """接入机构状态类型"""
    SHFE_FTDC_OS_Ready = 48
    """启用"""
    SHFE_FTDC_OS_CheckIn = 49
    """签到"""
    SHFE_FTDC_OS_CheckOut = 50
    """签退"""
    SHFE_FTDC_OS_CheckFileArrived = 51
    """对帐文件到达"""
    SHFE_FTDC_OS_CheckDetail = 52
    """对帐"""
    SHFE_FTDC_OS_DayEndClean = 53
    """日终清理"""
    SHFE_FTDC_OS_Invalid = 57
    """注销"""
    SHFE_FTDC_OS_NULL = 0


class TShfeFtdcCCBFeeModeType(Enum):
    """建行收费模式类型"""
    SHFE_FTDC_CCBFM_ByAmount = 49
    """按金额扣收"""
    SHFE_FTDC_CCBFM_ByMonth = 50
    """按月扣收"""
    SHFE_FTDC_CCBFM_NULL = 0


class TShfeFtdcCommApiTypeType(Enum):
    """通讯API类型类型"""
    SHFE_FTDC_CAPIT_Client = 49
    """客户端"""
    SHFE_FTDC_CAPIT_Server = 50
    """服务端"""
    SHFE_FTDC_CAPIT_UserApi = 51
    """交易系统的UserApi"""
    SHFE_FTDC_CAPIT_NULL = 0


class TShfeFtdcLinkStatusType(Enum):
    """连接状态类型"""
    SHFE_FTDC_LS_Connected = 49
    """已经连接"""
    SHFE_FTDC_LS_Disconnected = 50
    """没有连接"""
    SHFE_FTDC_LS_NULL = 0


class TShfeFtdcPwdFlagType(Enum):
    """密码核对标志类型"""
    SHFE_FTDC_BPWDF_NoCheck = 48
    """不核对"""
    SHFE_FTDC_BPWDF_BlankCheck = 49
    """明文核对"""
    SHFE_FTDC_BPWDF_EncryptCheck = 50
    """密文核对"""
    SHFE_FTDC_BPWDF_NULL = 0


class TShfeFtdcSecuAccTypeType(Enum):
    """期货帐号类型类型"""
    SHFE_FTDC_SAT_AccountID = 49
    """资金帐号"""
    SHFE_FTDC_SAT_CardID = 50
    """资金卡号"""
    SHFE_FTDC_SAT_SHStockholderID = 51
    """上海股东帐号"""
    SHFE_FTDC_SAT_SZStockholderID = 52
    """深圳股东帐号"""
    SHFE_FTDC_SAT_NULL = 0


class TShfeFtdcTransferStatusType(Enum):
    """转账交易状态类型"""
    SHFE_FTDC_TRFS_Normal = 48
    """正常"""
    SHFE_FTDC_TRFS_Repealed = 49
    """被冲正"""
    SHFE_FTDC_TRFS_NULL = 0


class TShfeFtdcSponsorTypeType(Enum):
    """发起方类型"""
    SHFE_FTDC_SPTYPE_Broker = 48
    """期商"""
    SHFE_FTDC_SPTYPE_Bank = 49
    """银行"""
    SHFE_FTDC_SPTYPE_NULL = 0


class TShfeFtdcReqRspTypeType(Enum):
    """请求响应类别类型"""
    SHFE_FTDC_REQRSP_Request = 48
    """请求"""
    SHFE_FTDC_REQRSP_Response = 49
    """响应"""
    SHFE_FTDC_REQRSP_NULL = 0


class TShfeFtdcFBTUserEventTypeType(Enum):
    """银期转帐用户事件类型类型"""
    SHFE_FTDC_FBTUET_SignIn = 48
    """签到"""
    SHFE_FTDC_FBTUET_FromBankToFuture = 49
    """银行转期货"""
    SHFE_FTDC_FBTUET_FromFutureToBank = 50
    """期货转银行"""
    SHFE_FTDC_FBTUET_OpenAccount = 51
    """开户"""
    SHFE_FTDC_FBTUET_CancelAccount = 52
    """销户"""
    SHFE_FTDC_FBTUET_ChangeAccount = 53
    """变更银行账户"""
    SHFE_FTDC_FBTUET_RepealFromBankToFuture = 54
    """冲正银行转期货"""
    SHFE_FTDC_FBTUET_RepealFromFutureToBank = 55
    """冲正期货转银行"""
    SHFE_FTDC_FBTUET_QueryBankAccount = 56
    """查询银行账户"""
    SHFE_FTDC_FBTUET_QueryFutureAccount = 57
    """查询期货账户"""
    SHFE_FTDC_FBTUET_SignOut = 65
    """签退"""
    SHFE_FTDC_FBTUET_SyncKey = 66
    """密钥同步"""
    SHFE_FTDC_FBTUET_ReserveOpenAccount = 67
    """预约开户"""
    SHFE_FTDC_FBTUET_CancelReserveOpenAccount = 68
    """撤销预约开户"""
    SHFE_FTDC_FBTUET_ReserveOpenAccountConfirm = 69
    """预约开户确认"""
    SHFE_FTDC_FBTUET_Other = 90
    """其他"""
    SHFE_FTDC_FBTUET_NULL = 0


class TShfeFtdcDBOperationType(Enum):
    """记录操作类型类型"""
    SHFE_FTDC_DBOP_Insert = 48
    """插入"""
    SHFE_FTDC_DBOP_Update = 49
    """更新"""
    SHFE_FTDC_DBOP_Delete = 50
    """删除"""
    SHFE_FTDC_DBOP_NULL = 0


class TShfeFtdcSyncFlagType(Enum):
    """同步标记类型"""
    SHFE_FTDC_SYNF_Yes = 48
    """已同步"""
    SHFE_FTDC_SYNF_No = 49
    """未同步"""
    SHFE_FTDC_SYNF_NULL = 0


class TShfeFtdcSyncTypeType(Enum):
    """同步类型类型"""
    SHFE_FTDC_SYNT_OneOffSync = 48
    """一次同步"""
    SHFE_FTDC_SYNT_TimerSync = 49
    """定时同步"""
    SHFE_FTDC_SYNT_TimerFullSync = 50
    """定时完全同步"""
    SHFE_FTDC_SYNT_NULL = 0


class TShfeFtdcExDirectionType(Enum):
    """换汇方向类型"""
    SHFE_FTDC_FBEDIR_Settlement = 48
    """结汇"""
    SHFE_FTDC_FBEDIR_Sale = 49
    """售汇"""
    SHFE_FTDC_FBEDIR_NULL = 0


class TShfeFtdcFBEResultFlagType(Enum):
    """换汇成功标志类型"""
    SHFE_FTDC_FBERES_Success = 48
    """成功"""
    SHFE_FTDC_FBERES_InsufficientBalance = 49
    """账户余额不足"""
    SHFE_FTDC_FBERES_UnknownTrading = 56
    """交易结果未知"""
    SHFE_FTDC_FBERES_Fail = 120
    """失败"""
    SHFE_FTDC_FBERES_NULL = 0


class TShfeFtdcFBEExchStatusType(Enum):
    """换汇交易状态类型"""
    SHFE_FTDC_FBEES_Normal = 48
    """正常"""
    SHFE_FTDC_FBEES_ReExchange = 49
    """交易重发"""
    SHFE_FTDC_FBEES_NULL = 0


class TShfeFtdcFBEFileFlagType(Enum):
    """换汇文件标志类型"""
    SHFE_FTDC_FBEFG_DataPackage = 48
    """数据包"""
    SHFE_FTDC_FBEFG_File = 49
    """文件"""
    SHFE_FTDC_FBEFG_NULL = 0


class TShfeFtdcFBEAlreadyTradeType(Enum):
    """换汇已交易标志类型"""
    SHFE_FTDC_FBEAT_NotTrade = 48
    """未交易"""
    SHFE_FTDC_FBEAT_Trade = 49
    """已交易"""
    SHFE_FTDC_FBEAT_NULL = 0


class TShfeFtdcFBEUserEventTypeType(Enum):
    """银期换汇用户事件类型类型"""
    SHFE_FTDC_FBEUET_SignIn = 48
    """签到"""
    SHFE_FTDC_FBEUET_Exchange = 49
    """换汇"""
    SHFE_FTDC_FBEUET_ReExchange = 50
    """换汇重发"""
    SHFE_FTDC_FBEUET_QueryBankAccount = 51
    """银行账户查询"""
    SHFE_FTDC_FBEUET_QueryExchDetial = 52
    """换汇明细查询"""
    SHFE_FTDC_FBEUET_QueryExchSummary = 53
    """换汇汇总查询"""
    SHFE_FTDC_FBEUET_QueryExchRate = 54
    """换汇汇率查询"""
    SHFE_FTDC_FBEUET_CheckBankAccount = 55
    """对账文件通知"""
    SHFE_FTDC_FBEUET_SignOut = 56
    """签退"""
    SHFE_FTDC_FBEUET_Other = 90
    """其他"""
    SHFE_FTDC_FBEUET_NULL = 0


class TShfeFtdcFBEReqFlagType(Enum):
    """换汇发送标志类型"""
    SHFE_FTDC_FBERF_UnProcessed = 48
    """未处理"""
    SHFE_FTDC_FBERF_WaitSend = 49
    """等待发送"""
    SHFE_FTDC_FBERF_SendSuccess = 50
    """发送成功"""
    SHFE_FTDC_FBERF_SendFailed = 51
    """发送失败"""
    SHFE_FTDC_FBERF_WaitReSend = 52
    """等待重发"""
    SHFE_FTDC_FBERF_NULL = 0


class TShfeFtdcNotifyClassType(Enum):
    """风险通知类型类型"""
    SHFE_FTDC_NC_NOERROR = 48
    """正常"""
    SHFE_FTDC_NC_Warn = 49
    """警示"""
    SHFE_FTDC_NC_Call = 50
    """追保"""
    SHFE_FTDC_NC_Force = 51
    """强平"""
    SHFE_FTDC_NC_CHUANCANG = 52
    """穿仓"""
    SHFE_FTDC_NC_Exception = 53
    """异常"""
    SHFE_FTDC_NC_NULL = 0


class TShfeFtdcForceCloseTypeType(Enum):
    """强平单类型类型"""
    SHFE_FTDC_FCT_Manual = 48
    """手工强平"""
    SHFE_FTDC_FCT_Single = 49
    """单一投资者辅助强平"""
    SHFE_FTDC_FCT_Group = 50
    """批量投资者辅助强平"""
    SHFE_FTDC_FCT_NULL = 0


class TShfeFtdcRiskNotifyMethodType(Enum):
    """风险通知途径类型"""
    SHFE_FTDC_RNM_System = 48
    """系统通知"""
    SHFE_FTDC_RNM_SMS = 49
    """短信通知"""
    SHFE_FTDC_RNM_EMail = 50
    """邮件通知"""
    SHFE_FTDC_RNM_Manual = 51
    """人工通知"""
    SHFE_FTDC_RNM_NULL = 0


class TShfeFtdcRiskNotifyStatusType(Enum):
    """风险通知状态类型"""
    SHFE_FTDC_RNS_NotGen = 48
    """未生成"""
    SHFE_FTDC_RNS_Generated = 49
    """已生成未发送"""
    SHFE_FTDC_RNS_SendError = 50
    """发送失败"""
    SHFE_FTDC_RNS_SendOk = 51
    """已发送未接收"""
    SHFE_FTDC_RNS_Received = 52
    """已接收未确认"""
    SHFE_FTDC_RNS_Confirmed = 53
    """已确认"""
    SHFE_FTDC_RNS_NULL = 0


class TShfeFtdcRiskUserEventType(Enum):
    """风控用户操作事件类型"""
    SHFE_FTDC_RUE_ExportData = 48
    """导出数据"""
    SHFE_FTDC_RUE_NULL = 0


class TShfeFtdcConditionalOrderSortTypeType(Enum):
    """条件单索引条件类型"""
    SHFE_FTDC_COST_LastPriceAsc = 48
    """使用最新价升序"""
    SHFE_FTDC_COST_LastPriceDesc = 49
    """使用最新价降序"""
    SHFE_FTDC_COST_AskPriceAsc = 50
    """使用卖价升序"""
    SHFE_FTDC_COST_AskPriceDesc = 51
    """使用卖价降序"""
    SHFE_FTDC_COST_BidPriceAsc = 52
    """使用买价升序"""
    SHFE_FTDC_COST_BidPriceDesc = 53
    """使用买价降序"""
    SHFE_FTDC_COST_NULL = 0


class TShfeFtdcSendTypeType(Enum):
    """报送状态类型"""
    SHFE_FTDC_UOAST_NoSend = 48
    """未发送"""
    SHFE_FTDC_UOAST_Sended = 49
    """已发送"""
    SHFE_FTDC_UOAST_Generated = 50
    """已生成"""
    SHFE_FTDC_UOAST_SendFail = 51
    """报送失败"""
    SHFE_FTDC_UOAST_Success = 52
    """接收成功"""
    SHFE_FTDC_UOAST_Fail = 53
    """接收失败"""
    SHFE_FTDC_UOAST_Cancel = 54
    """取消报送"""
    SHFE_FTDC_UOAST_NULL = 0


class TShfeFtdcClientIDStatusType(Enum):
    """交易编码状态类型"""
    SHFE_FTDC_UOACS_NoApply = 49
    """未申请"""
    SHFE_FTDC_UOACS_Submited = 50
    """已提交申请"""
    SHFE_FTDC_UOACS_Sended = 51
    """已发送申请"""
    SHFE_FTDC_UOACS_Success = 52
    """完成"""
    SHFE_FTDC_UOACS_Refuse = 53
    """拒绝"""
    SHFE_FTDC_UOACS_Cancel = 54
    """已撤销编码"""
    SHFE_FTDC_UOACS_NULL = 0


class TShfeFtdcQuestionTypeType(Enum):
    """特有信息类型类型"""
    SHFE_FTDC_QT_Radio = 49
    """单选"""
    SHFE_FTDC_QT_Option = 50
    """多选"""
    SHFE_FTDC_QT_Blank = 51
    """填空"""
    SHFE_FTDC_QT_NULL = 0


class TShfeFtdcBusinessTypeType(Enum):
    """业务类型类型"""
    SHFE_FTDC_BT_Request = 49
    """请求"""
    SHFE_FTDC_BT_Response = 50
    """应答"""
    SHFE_FTDC_BT_Notice = 51
    """通知"""
    SHFE_FTDC_BT_NULL = 0


class TShfeFtdcCfmmcReturnCodeType(Enum):
    """监控中心返回码类型"""
    SHFE_FTDC_CRC_Success = 48
    """成功"""
    SHFE_FTDC_CRC_Working = 49
    """该客户已经有流程在处理中"""
    SHFE_FTDC_CRC_InfoFail = 50
    """监控中客户资料检查失败"""
    SHFE_FTDC_CRC_IDCardFail = 51
    """监控中实名制检查失败"""
    SHFE_FTDC_CRC_OtherFail = 52
    """其他错误"""
    SHFE_FTDC_CRC_NULL = 0


class TShfeFtdcClientTypeType(Enum):
    """客户类型类型"""
    SHFE_FTDC_CfMMCCT_All = 48
    """所有"""
    SHFE_FTDC_CfMMCCT_Person = 49
    """个人"""
    SHFE_FTDC_CfMMCCT_Company = 50
    """单位"""
    SHFE_FTDC_CfMMCCT_Other = 51
    """其他"""
    SHFE_FTDC_CfMMCCT_SpecialOrgan = 52
    """特殊法人"""
    SHFE_FTDC_CfMMCCT_Asset = 53
    """资管户"""
    SHFE_FTDC_CfMMCCT_NULL = 0


class TShfeFtdcExchangeIDTypeType(Enum):
    """交易所编号类型"""
    SHFE_FTDC_EIDT_SHFE = 83
    """上海期货交易所"""
    SHFE_FTDC_EIDT_CZCE = 90
    """郑州商品交易所"""
    SHFE_FTDC_EIDT_DCE = 68
    """大连商品交易所"""
    SHFE_FTDC_EIDT_CFFEX = 74
    """中国金融期货交易所"""
    SHFE_FTDC_EIDT_INE = 78
    """上海国际能源交易中心股份有限公司"""
    SHFE_FTDC_EIDT_NULL = 0


class TShfeFtdcExClientIDTypeType(Enum):
    """交易编码类型类型"""
    SHFE_FTDC_ECIDT_Hedge = 49
    """套保"""
    SHFE_FTDC_ECIDT_Arbitrage = 50
    """套利"""
    SHFE_FTDC_ECIDT_Speculation = 51
    """投机"""
    SHFE_FTDC_ECIDT_NULL = 0


class TShfeFtdcUpdateFlagType(Enum):
    """更新状态类型"""
    SHFE_FTDC_UF_NoUpdate = 48
    """未更新"""
    SHFE_FTDC_UF_Success = 49
    """更新全部信息成功"""
    SHFE_FTDC_UF_Fail = 50
    """更新全部信息失败"""
    SHFE_FTDC_UF_TCSuccess = 51
    """更新交易编码成功"""
    SHFE_FTDC_UF_TCFail = 52
    """更新交易编码失败"""
    SHFE_FTDC_UF_Cancel = 53
    """已丢弃"""
    SHFE_FTDC_UF_NULL = 0


class TShfeFtdcApplyOperateIDType(Enum):
    """申请动作类型"""
    SHFE_FTDC_AOID_OpenInvestor = 49
    """开户"""
    SHFE_FTDC_AOID_ModifyIDCard = 50
    """修改身份信息"""
    SHFE_FTDC_AOID_ModifyNoIDCard = 51
    """修改一般信息"""
    SHFE_FTDC_AOID_ApplyTradingCode = 52
    """申请交易编码"""
    SHFE_FTDC_AOID_CancelTradingCode = 53
    """撤销交易编码"""
    SHFE_FTDC_AOID_CancelInvestor = 54
    """销户"""
    SHFE_FTDC_AOID_FreezeAccount = 56
    """账户休眠"""
    SHFE_FTDC_AOID_ActiveFreezeAccount = 57
    """激活休眠账户"""
    SHFE_FTDC_AOID_NULL = 0


class TShfeFtdcApplyStatusIDType(Enum):
    """申请状态类型"""
    SHFE_FTDC_ASID_NoComplete = 49
    """未补全"""
    SHFE_FTDC_ASID_Submited = 50
    """已提交"""
    SHFE_FTDC_ASID_Checked = 51
    """已审核"""
    SHFE_FTDC_ASID_Refused = 52
    """已拒绝"""
    SHFE_FTDC_ASID_Deleted = 53
    """已删除"""
    SHFE_FTDC_ASID_NULL = 0


class TShfeFtdcSendMethodType(Enum):
    """发送方式类型"""
    SHFE_FTDC_UOASM_ByAPI = 49
    """文件发送"""
    SHFE_FTDC_UOASM_ByFile = 50
    """电子发送"""
    SHFE_FTDC_UOASM_NULL = 0


class TShfeFtdcEventModeType(Enum):
    """操作方法类型"""
    SHFE_FTDC_EvM_ADD = 49
    """增加"""
    SHFE_FTDC_EvM_UPDATE = 50
    """修改"""
    SHFE_FTDC_EvM_DELETE = 51
    """删除"""
    SHFE_FTDC_EvM_CHECK = 52
    """复核"""
    SHFE_FTDC_EvM_COPY = 53
    """复制"""
    SHFE_FTDC_EvM_CANCEL = 54
    """注销"""
    SHFE_FTDC_EvM_Reverse = 55
    """冲销"""
    SHFE_FTDC_EvM_NULL = 0


class TShfeFtdcUOAAutoSendType(Enum):
    """统一开户申请自动发送类型"""
    SHFE_FTDC_UOAA_ASR = 49
    """自动发送并接收"""
    SHFE_FTDC_UOAA_ASNR = 50
    """自动发送，不自动接收"""
    SHFE_FTDC_UOAA_NSAR = 51
    """不自动发送，自动接收"""
    SHFE_FTDC_UOAA_NSR = 52
    """不自动发送，也不自动接收"""
    SHFE_FTDC_UOAA_NULL = 0


class TShfeFtdcFlowIDType(Enum):
    """流程ID类型"""
    SHFE_FTDC_EvM_InvestorGroupFlow = 49
    """投资者对应投资者组设置"""
    SHFE_FTDC_EvM_InvestorRate = 50
    """投资者手续费率设置"""
    SHFE_FTDC_EvM_InvestorCommRateModel = 51
    """投资者手续费率模板关系设置"""
    SHFE_FTDC_EvM_NULL = 0


class TShfeFtdcCheckLevelType(Enum):
    """复核级别类型"""
    SHFE_FTDC_CL_Zero = 48
    """零级复核"""
    SHFE_FTDC_CL_One = 49
    """一级复核"""
    SHFE_FTDC_CL_Two = 50
    """二级复核"""
    SHFE_FTDC_CL_NULL = 0


class TShfeFtdcCheckStatusType(Enum):
    """复核级别类型"""
    SHFE_FTDC_CHS_Init = 48
    """未复核"""
    SHFE_FTDC_CHS_Checking = 49
    """复核中"""
    SHFE_FTDC_CHS_Checked = 50
    """已复核"""
    SHFE_FTDC_CHS_Refuse = 51
    """拒绝"""
    SHFE_FTDC_CHS_Cancel = 52
    """作废"""
    SHFE_FTDC_CHS_NULL = 0


class TShfeFtdcUsedStatusType(Enum):
    """生效状态类型"""
    SHFE_FTDC_CHU_Unused = 48
    """未生效"""
    SHFE_FTDC_CHU_Used = 49
    """已生效"""
    SHFE_FTDC_CHU_Fail = 50
    """生效失败"""
    SHFE_FTDC_CHU_NULL = 0


class TShfeFtdcBankAcountOriginType(Enum):
    """账户来源类型"""
    SHFE_FTDC_BAO_ByAccProperty = 48
    """手工录入"""
    SHFE_FTDC_BAO_ByFBTransfer = 49
    """银期转账"""
    SHFE_FTDC_BAO_NULL = 0


class TShfeFtdcMonthBillTradeSumType(Enum):
    """结算单月报成交汇总方式类型"""
    SHFE_FTDC_MBTS_ByInstrument = 48
    """同日同合约"""
    SHFE_FTDC_MBTS_ByDayInsPrc = 49
    """同日同合约同价格"""
    SHFE_FTDC_MBTS_ByDayIns = 50
    """同合约"""
    SHFE_FTDC_MBTS_NULL = 0


class TShfeFtdcFBTTradeCodeEnumType(Enum):
    """银期交易代码枚举类型"""
    SHFE_FTDC_FTC_BankLaunchBankToBroker = 49
    """银行发起银行转期货"""
    SHFE_FTDC_FTC_BrokerLaunchBankToBroker = 49
    """期货发起银行转期货"""
    SHFE_FTDC_FTC_BankLaunchBrokerToBank = 50
    """银行发起期货转银行"""
    SHFE_FTDC_FTC_BrokerLaunchBrokerToBank = 50
    """期货发起期货转银行"""
    SHFE_FTDC_FTC_NULL = 0


class TShfeFtdcOTPTypeType(Enum):
    """动态令牌类型类型"""
    SHFE_FTDC_OTP_NONE = 48
    """无动态令牌"""
    SHFE_FTDC_OTP_TOTP = 49
    """时间令牌"""
    SHFE_FTDC_OTP_NULL = 0


class TShfeFtdcOTPStatusType(Enum):
    """动态令牌状态类型"""
    SHFE_FTDC_OTPS_Unused = 48
    """未使用"""
    SHFE_FTDC_OTPS_Used = 49
    """已使用"""
    SHFE_FTDC_OTPS_Disuse = 50
    """注销"""
    SHFE_FTDC_OTPS_NULL = 0


class TShfeFtdcBrokerUserTypeType(Enum):
    """经济公司用户类型类型"""
    SHFE_FTDC_BUT_Investor = 49
    """投资者"""
    SHFE_FTDC_BUT_BrokerUser = 50
    """操作员"""
    SHFE_FTDC_BUT_NULL = 0


class TShfeFtdcFutureTypeType(Enum):
    """期货类型类型"""
    SHFE_FTDC_FUTT_Commodity = 49
    """商品期货"""
    SHFE_FTDC_FUTT_Financial = 50
    """金融期货"""
    SHFE_FTDC_FUTT_NULL = 0


class TShfeFtdcFundEventTypeType(Enum):
    """资金管理操作类型类型"""
    SHFE_FTDC_FET_Restriction = 48
    """转账限额"""
    SHFE_FTDC_FET_TodayRestriction = 49
    """当日转账限额"""
    SHFE_FTDC_FET_Transfer = 50
    """期商流水"""
    SHFE_FTDC_FET_Credit = 51
    """资金冻结"""
    SHFE_FTDC_FET_InvestorWithdrawAlm = 52
    """投资者可提资金比例"""
    SHFE_FTDC_FET_BankRestriction = 53
    """单个银行帐户转账限额"""
    SHFE_FTDC_FET_Accountregister = 54
    """银期签约账户"""
    SHFE_FTDC_FET_ExchangeFundIO = 55
    """交易所出入金"""
    SHFE_FTDC_FET_InvestorFundIO = 56
    """投资者出入金"""
    SHFE_FTDC_FET_NULL = 0


class TShfeFtdcAccountSourceTypeType(Enum):
    """资金账户来源类型"""
    SHFE_FTDC_AST_FBTransfer = 48
    """银期同步"""
    SHFE_FTDC_AST_ManualEntry = 49
    """手工录入"""
    SHFE_FTDC_AST_NULL = 0


class TShfeFtdcCodeSourceTypeType(Enum):
    """交易编码来源类型"""
    SHFE_FTDC_CST_UnifyAccount = 48
    """统一开户(已规范)"""
    SHFE_FTDC_CST_ManualEntry = 49
    """手工录入(未规范)"""
    SHFE_FTDC_CST_NULL = 0


class TShfeFtdcUserRangeType(Enum):
    """操作员范围类型"""
    SHFE_FTDC_UR_All = 48
    """所有"""
    SHFE_FTDC_UR_Single = 49
    """单一操作员"""
    SHFE_FTDC_UR_NULL = 0


class TShfeFtdcByGroupType(Enum):
    """交易统计表按客户统计方式类型"""
    SHFE_FTDC_BG_Investor = 50
    """按投资者统计"""
    SHFE_FTDC_BG_Group = 49
    """按类统计"""
    SHFE_FTDC_BG_NULL = 0


class TShfeFtdcTradeSumStatModeType(Enum):
    """交易统计表按范围统计方式类型"""
    SHFE_FTDC_TSSM_Instrument = 49
    """按合约统计"""
    SHFE_FTDC_TSSM_Product = 50
    """按产品统计"""
    SHFE_FTDC_TSSM_Exchange = 51
    """按交易所统计"""
    SHFE_FTDC_TSSM_NULL = 0


class TShfeFtdcExprSetModeType(Enum):
    """日期表达式设置类型类型"""
    SHFE_FTDC_ESM_Relative = 49
    """相对已有规则设置"""
    SHFE_FTDC_ESM_Typical = 50
    """典型设置"""
    SHFE_FTDC_ESM_NULL = 0


class TShfeFtdcRateInvestorRangeType(Enum):
    """投资者范围类型"""
    SHFE_FTDC_RIR_All = 49
    """公司标准"""
    SHFE_FTDC_RIR_Model = 50
    """模板"""
    SHFE_FTDC_RIR_Single = 51
    """单一投资者"""
    SHFE_FTDC_RIR_NULL = 0


class TShfeFtdcSyncDataStatusType(Enum):
    """主次用系统数据同步状态类型"""
    SHFE_FTDC_SDS_Initialize = 48
    """未同步"""
    SHFE_FTDC_SDS_Settlementing = 49
    """同步中"""
    SHFE_FTDC_SDS_Settlemented = 50
    """已同步"""
    SHFE_FTDC_SDS_NULL = 0


class TShfeFtdcTradeSourceType(Enum):
    """成交来源类型"""
    SHFE_FTDC_TSRC_NORMAL = 48
    """来自交易所普通回报"""
    SHFE_FTDC_TSRC_QUERY = 49
    """来自查询"""
    SHFE_FTDC_TSRC_NULL = 0


class TShfeFtdcFlexStatModeType(Enum):
    """产品合约统计方式类型"""
    SHFE_FTDC_FSM_Product = 49
    """产品统计"""
    SHFE_FTDC_FSM_Exchange = 50
    """交易所统计"""
    SHFE_FTDC_FSM_All = 51
    """统计所有"""
    SHFE_FTDC_FSM_NULL = 0


class TShfeFtdcByInvestorRangeType(Enum):
    """投资者范围统计方式类型"""
    SHFE_FTDC_BIR_Property = 49
    """属性统计"""
    SHFE_FTDC_BIR_All = 50
    """统计所有"""
    SHFE_FTDC_BIR_NULL = 0


class TShfeFtdcPropertyInvestorRangeType(Enum):
    """投资者范围类型"""
    SHFE_FTDC_PIR_All = 49
    """所有"""
    SHFE_FTDC_PIR_Property = 50
    """投资者属性"""
    SHFE_FTDC_PIR_Single = 51
    """单一投资者"""
    SHFE_FTDC_PIR_NULL = 0


class TShfeFtdcFileStatusType(Enum):
    """文件状态类型"""
    SHFE_FTDC_FIS_NoCreate = 48
    """未生成"""
    SHFE_FTDC_FIS_Created = 49
    """已生成"""
    SHFE_FTDC_FIS_Failed = 50
    """生成失败"""
    SHFE_FTDC_FIS_NULL = 0


class TShfeFtdcFileGenStyleType(Enum):
    """文件生成方式类型"""
    SHFE_FTDC_FGS_FileTransmit = 48
    """下发"""
    SHFE_FTDC_FGS_FileGen = 49
    """生成"""
    SHFE_FTDC_FGS_NULL = 0


class TShfeFtdcSysOperModeType(Enum):
    """系统日志操作方法类型"""
    SHFE_FTDC_SoM_Add = 49
    """增加"""
    SHFE_FTDC_SoM_Update = 50
    """修改"""
    SHFE_FTDC_SoM_Delete = 51
    """删除"""
    SHFE_FTDC_SoM_Copy = 52
    """复制"""
    SHFE_FTDC_SoM_AcTive = 53
    """激活"""
    SHFE_FTDC_SoM_CanCel = 54
    """注销"""
    SHFE_FTDC_SoM_ReSet = 55
    """重置"""
    SHFE_FTDC_SoM_NULL = 0


class TShfeFtdcSysOperTypeType(Enum):
    """系统日志操作类型类型"""
    SHFE_FTDC_SoT_UpdatePassword = 48
    """修改操作员密码"""
    SHFE_FTDC_SoT_UserDepartment = 49
    """操作员组织架构关系"""
    SHFE_FTDC_SoT_RoleManager = 50
    """角色管理"""
    SHFE_FTDC_SoT_RoleFunction = 51
    """角色功能设置"""
    SHFE_FTDC_SoT_BaseParam = 52
    """基础参数设置"""
    SHFE_FTDC_SoT_SetUserID = 53
    """设置操作员"""
    SHFE_FTDC_SoT_SetUserRole = 54
    """用户角色设置"""
    SHFE_FTDC_SoT_UserIpRestriction = 55
    """用户IP限制"""
    SHFE_FTDC_SoT_DepartmentManager = 56
    """组织架构管理"""
    SHFE_FTDC_SoT_DepartmentCopy = 57
    """组织架构向查询分类复制"""
    SHFE_FTDC_SoT_Tradingcode = 65
    """交易编码管理"""
    SHFE_FTDC_SoT_InvestorStatus = 66
    """投资者状态维护"""
    SHFE_FTDC_SoT_InvestorAuthority = 67
    """投资者权限管理"""
    SHFE_FTDC_SoT_PropertySet = 68
    """属性设置"""
    SHFE_FTDC_SoT_ReSetInvestorPasswd = 69
    """重置投资者密码"""
    SHFE_FTDC_SoT_InvestorPersonalityInfo = 70
    """投资者个性信息维护"""
    SHFE_FTDC_SoT_NULL = 0


class TShfeFtdcCSRCDataQueyTypeType(Enum):
    """上报数据查询类型类型"""
    SHFE_FTDC_CSRCQ_Current = 48
    """查询当前交易日报送的数据"""
    SHFE_FTDC_CSRCQ_History = 49
    """查询历史报送的代理经纪公司的数据"""
    SHFE_FTDC_CSRCQ_NULL = 0


class TShfeFtdcFreezeStatusType(Enum):
    """休眠状态类型"""
    SHFE_FTDC_FRS_Normal = 49
    """活跃"""
    SHFE_FTDC_FRS_Freeze = 48
    """休眠"""
    SHFE_FTDC_FRS_NULL = 0


class TShfeFtdcStandardStatusType(Enum):
    """规范状态类型"""
    SHFE_FTDC_STST_Standard = 48
    """已规范"""
    SHFE_FTDC_STST_NonStandard = 49
    """未规范"""
    SHFE_FTDC_STST_NULL = 0


class TShfeFtdcRightParamTypeType(Enum):
    """配置类型类型"""
    SHFE_FTDC_RPT_Freeze = 49
    """休眠户"""
    SHFE_FTDC_RPT_FreezeActive = 50
    """激活休眠户"""
    SHFE_FTDC_RPT_OpenLimit = 51
    """开仓权限限制"""
    SHFE_FTDC_RPT_RelieveOpenLimit = 52
    """解除开仓权限限制"""
    SHFE_FTDC_RPT_NULL = 0


class TShfeFtdcDataStatusType(Enum):
    """反洗钱审核表数据状态类型"""
    SHFE_FTDC_AMLDS_Normal = 48
    """正常"""
    SHFE_FTDC_AMLDS_Deleted = 49
    """已删除"""
    SHFE_FTDC_AMLDS_NULL = 0


class TShfeFtdcAMLCheckStatusType(Enum):
    """审核状态类型"""
    SHFE_FTDC_AMLCHS_Init = 48
    """未复核"""
    SHFE_FTDC_AMLCHS_Checking = 49
    """复核中"""
    SHFE_FTDC_AMLCHS_Checked = 50
    """已复核"""
    SHFE_FTDC_AMLCHS_RefuseReport = 51
    """拒绝上报"""
    SHFE_FTDC_AMLCHS_NULL = 0


class TShfeFtdcAmlDateTypeType(Enum):
    """日期类型类型"""
    SHFE_FTDC_AMLDT_DrawDay = 48
    """检查日期"""
    SHFE_FTDC_AMLDT_TouchDay = 49
    """发生日期"""
    SHFE_FTDC_AMLDT_NULL = 0


class TShfeFtdcAmlCheckLevelType(Enum):
    """审核级别类型"""
    SHFE_FTDC_AMLCL_CheckLevel0 = 48
    """零级审核"""
    SHFE_FTDC_AMLCL_CheckLevel1 = 49
    """一级审核"""
    SHFE_FTDC_AMLCL_CheckLevel2 = 50
    """二级审核"""
    SHFE_FTDC_AMLCL_CheckLevel3 = 51
    """三级审核"""
    SHFE_FTDC_AMLCL_NULL = 0


class TShfeFtdcExportFileTypeType(Enum):
    """导出文件类型类型"""
    SHFE_FTDC_EFT_CSV = 48
    """CSV"""
    SHFE_FTDC_EFT_EXCEL = 49
    """Excel"""
    SHFE_FTDC_EFT_DBF = 50
    """DBF"""
    SHFE_FTDC_EFT_NULL = 0


class TShfeFtdcSettleManagerTypeType(Enum):
    """结算配置类型类型"""
    SHFE_FTDC_SMT_Before = 49
    """结算前准备"""
    SHFE_FTDC_SMT_Settlement = 50
    """结算"""
    SHFE_FTDC_SMT_After = 51
    """结算后核对"""
    SHFE_FTDC_SMT_Settlemented = 52
    """结算后处理"""
    SHFE_FTDC_SMT_NULL = 0


class TShfeFtdcSettleManagerLevelType(Enum):
    """结算配置等级类型"""
    SHFE_FTDC_SML_Must = 49
    """必要"""
    SHFE_FTDC_SML_Alarm = 50
    """警告"""
    SHFE_FTDC_SML_Prompt = 51
    """提示"""
    SHFE_FTDC_SML_Ignore = 52
    """不检查"""
    SHFE_FTDC_SML_NULL = 0


class TShfeFtdcSettleManagerGroupType(Enum):
    """模块分组类型"""
    SHFE_FTDC_SMG_Exhcange = 49
    """交易所核对"""
    SHFE_FTDC_SMG_ASP = 50
    """内部核对"""
    SHFE_FTDC_SMG_CSRC = 51
    """上报数据核对"""
    SHFE_FTDC_SMG_NULL = 0


class TShfeFtdcLimitUseTypeType(Enum):
    """保值额度使用类型类型"""
    SHFE_FTDC_LUT_Repeatable = 49
    """可重复使用"""
    SHFE_FTDC_LUT_Unrepeatable = 50
    """不可重复使用"""
    SHFE_FTDC_LUT_NULL = 0


class TShfeFtdcDataResourceType(Enum):
    """数据来源类型"""
    SHFE_FTDC_DAR_Settle = 49
    """本系统"""
    SHFE_FTDC_DAR_Exchange = 50
    """交易所"""
    SHFE_FTDC_DAR_CSRC = 51
    """报送数据"""
    SHFE_FTDC_DAR_NULL = 0


class TShfeFtdcMarginTypeType(Enum):
    """保证金类型类型"""
    SHFE_FTDC_MGT_ExchMarginRate = 48
    """交易所保证金率"""
    SHFE_FTDC_MGT_InstrMarginRate = 49
    """投资者保证金率"""
    SHFE_FTDC_MGT_InstrMarginRateTrade = 50
    """投资者交易保证金率"""
    SHFE_FTDC_MGT_NULL = 0


class TShfeFtdcActiveTypeType(Enum):
    """生效类型类型"""
    SHFE_FTDC_ACT_Intraday = 49
    """仅当日生效"""
    SHFE_FTDC_ACT_Long = 50
    """长期生效"""
    SHFE_FTDC_ACT_NULL = 0


class TShfeFtdcMarginRateTypeType(Enum):
    """冲突保证金率类型类型"""
    SHFE_FTDC_MRT_Exchange = 49
    """交易所保证金率"""
    SHFE_FTDC_MRT_Investor = 50
    """投资者保证金率"""
    SHFE_FTDC_MRT_InvestorTrade = 51
    """投资者交易保证金率"""
    SHFE_FTDC_MRT_NULL = 0


class TShfeFtdcBackUpStatusType(Enum):
    """备份数据状态类型"""
    SHFE_FTDC_BUS_UnBak = 48
    """未生成备份数据"""
    SHFE_FTDC_BUS_BakUp = 49
    """备份数据生成中"""
    SHFE_FTDC_BUS_BakUped = 50
    """已生成备份数据"""
    SHFE_FTDC_BUS_BakFail = 51
    """备份数据失败"""
    SHFE_FTDC_BUS_NULL = 0


class TShfeFtdcInitSettlementType(Enum):
    """结算初始化状态类型"""
    SHFE_FTDC_SIS_UnInitialize = 48
    """结算初始化未开始"""
    SHFE_FTDC_SIS_Initialize = 49
    """结算初始化中"""
    SHFE_FTDC_SIS_Initialized = 50
    """结算初始化完成"""
    SHFE_FTDC_SIS_NULL = 0


class TShfeFtdcReportStatusType(Enum):
    """报表数据生成状态类型"""
    SHFE_FTDC_SRS_NoCreate = 48
    """未生成报表数据"""
    SHFE_FTDC_SRS_Create = 49
    """报表数据生成中"""
    SHFE_FTDC_SRS_Created = 50
    """已生成报表数据"""
    SHFE_FTDC_SRS_CreateFail = 51
    """生成报表数据失败"""
    SHFE_FTDC_SRS_NULL = 0


class TShfeFtdcSaveStatusType(Enum):
    """数据归档状态类型"""
    SHFE_FTDC_SSS_UnSaveData = 48
    """归档未完成"""
    SHFE_FTDC_SSS_SaveDatad = 49
    """归档完成"""
    SHFE_FTDC_SSS_NULL = 0


class TShfeFtdcSettArchiveStatusType(Enum):
    """结算确认数据归档状态类型"""
    SHFE_FTDC_SAS_UnArchived = 48
    """未归档数据"""
    SHFE_FTDC_SAS_Archiving = 49
    """数据归档中"""
    SHFE_FTDC_SAS_Archived = 50
    """已归档数据"""
    SHFE_FTDC_SAS_ArchiveFail = 51
    """归档数据失败"""
    SHFE_FTDC_SAS_NULL = 0


class TShfeFtdcCTPTypeType(Enum):
    """CTP交易系统类型类型"""
    SHFE_FTDC_CTPT_Unkown = 48
    """未知类型"""
    SHFE_FTDC_CTPT_MainCenter = 49
    """主中心"""
    SHFE_FTDC_CTPT_BackUp = 50
    """备中心"""
    SHFE_FTDC_CTPT_NULL = 0


class TShfeFtdcCloseDealTypeType(Enum):
    """平仓处理类型类型"""
    SHFE_FTDC_CDT_Normal = 48
    """正常"""
    SHFE_FTDC_CDT_SpecFirst = 49
    """投机平仓优先"""
    SHFE_FTDC_CDT_NULL = 0


class TShfeFtdcMortgageFundUseRangeType(Enum):
    """货币质押资金可用范围类型"""
    SHFE_FTDC_MFUR_None = 48
    """不能使用"""
    SHFE_FTDC_MFUR_Margin = 49
    """用于保证金"""
    SHFE_FTDC_MFUR_All = 50
    """用于手续费、盈亏、保证金"""
    SHFE_FTDC_MFUR_NULL = 0


class TShfeFtdcSpecProductTypeType(Enum):
    """特殊产品类型类型"""
    SHFE_FTDC_SPT_CzceHedge = 49
    """郑商所套保产品"""
    SHFE_FTDC_SPT_IneForeignCurrency = 50
    """货币质押产品"""
    SHFE_FTDC_SPT_DceOpenClose = 51
    """大连短线开平仓产品"""
    SHFE_FTDC_SPT_NULL = 0


class TShfeFtdcFundMortgageTypeType(Enum):
    """货币质押类型类型"""
    SHFE_FTDC_FMT_Mortgage = 49
    """质押"""
    SHFE_FTDC_FMT_Redemption = 50
    """解质"""
    SHFE_FTDC_FMT_NULL = 0


class TShfeFtdcAccountSettlementParamIDType(Enum):
    """投资者账户结算参数代码类型"""
    SHFE_FTDC_ASPI_BaseMargin = 49
    """基础保证金"""
    SHFE_FTDC_ASPI_LowestInterest = 50
    """最低权益标准"""
    SHFE_FTDC_ASPI_NULL = 0


class TShfeFtdcFundMortDirectionType(Enum):
    """货币质押方向类型"""
    SHFE_FTDC_FMD_In = 49
    """货币质入"""
    SHFE_FTDC_FMD_Out = 50
    """货币质出"""
    SHFE_FTDC_FMD_NULL = 0


class TShfeFtdcBusinessClassType(Enum):
    """换汇类别类型"""
    SHFE_FTDC_BT_Profit = 48
    """盈利"""
    SHFE_FTDC_BT_Loss = 49
    """亏损"""
    SHFE_FTDC_BT_Other = 90
    """其他"""
    SHFE_FTDC_BT_NULL = 0


class TShfeFtdcSwapSourceTypeType(Enum):
    """换汇数据来源类型"""
    SHFE_FTDC_SST_Manual = 48
    """手工"""
    SHFE_FTDC_SST_Automatic = 49
    """自动生成"""
    SHFE_FTDC_SST_NULL = 0


class TShfeFtdcCurrExDirectionType(Enum):
    """换汇类型类型"""
    SHFE_FTDC_CED_Settlement = 48
    """结汇"""
    SHFE_FTDC_CED_Sale = 49
    """售汇"""
    SHFE_FTDC_CED_NULL = 0


class TShfeFtdcCurrencySwapStatusType(Enum):
    """申请状态类型"""
    SHFE_FTDC_CSS_Entry = 49
    """已录入"""
    SHFE_FTDC_CSS_Approve = 50
    """已审核"""
    SHFE_FTDC_CSS_Refuse = 51
    """已拒绝"""
    SHFE_FTDC_CSS_Revoke = 52
    """已撤销"""
    SHFE_FTDC_CSS_Send = 53
    """已发送"""
    SHFE_FTDC_CSS_Success = 54
    """换汇成功"""
    SHFE_FTDC_CSS_Failure = 55
    """换汇失败"""
    SHFE_FTDC_CSS_NULL = 0


class TShfeFtdcReqFlagType(Enum):
    """换汇发送标志类型"""
    SHFE_FTDC_REQF_NoSend = 48
    """未发送"""
    SHFE_FTDC_REQF_SendSuccess = 49
    """发送成功"""
    SHFE_FTDC_REQF_SendFailed = 50
    """发送失败"""
    SHFE_FTDC_REQF_WaitReSend = 51
    """等待重发"""
    SHFE_FTDC_REQF_NULL = 0


class TShfeFtdcResFlagType(Enum):
    """换汇返回成功标志类型"""
    SHFE_FTDC_RESF_Success = 48
    """成功"""
    SHFE_FTDC_RESF_InsuffiCient = 49
    """账户余额不足"""
    SHFE_FTDC_RESF_UnKnown = 56
    """交易结果未知"""
    SHFE_FTDC_RESF_NULL = 0


class TShfeFtdcExStatusType(Enum):
    """修改状态类型"""
    SHFE_FTDC_EXS_Before = 48
    """修改前"""
    SHFE_FTDC_EXS_After = 49
    """修改后"""
    SHFE_FTDC_EXS_NULL = 0


class TShfeFtdcClientRegionType(Enum):
    """开户客户地域类型"""
    SHFE_FTDC_CR_Domestic = 49
    """国内客户"""
    SHFE_FTDC_CR_GMT = 50
    """港澳台客户"""
    SHFE_FTDC_CR_Foreign = 51
    """国外客户"""
    SHFE_FTDC_CR_NULL = 0


class TShfeFtdcHasBoardType(Enum):
    """是否有董事会类型"""
    SHFE_FTDC_HB_No = 48
    """没有"""
    SHFE_FTDC_HB_Yes = 49
    """有"""
    SHFE_FTDC_HB_NULL = 0


class TShfeFtdcStartModeType(Enum):
    """启动模式类型"""
    SHFE_FTDC_SM_Normal = 49
    """正常"""
    SHFE_FTDC_SM_Emerge = 50
    """应急"""
    SHFE_FTDC_SM_Restore = 51
    """恢复"""
    SHFE_FTDC_SM_NULL = 0


class TShfeFtdcTemplateTypeType(Enum):
    """模型类型类型"""
    SHFE_FTDC_TPT_Full = 49
    """全量"""
    SHFE_FTDC_TPT_Increment = 50
    """增量"""
    SHFE_FTDC_TPT_BackUp = 51
    """备份"""
    SHFE_FTDC_TPT_NULL = 0


class TShfeFtdcLoginModeType(Enum):
    """登录模式类型"""
    SHFE_FTDC_LM_Trade = 48
    """交易"""
    SHFE_FTDC_LM_Transfer = 49
    """转账"""
    SHFE_FTDC_LM_NULL = 0


class TShfeFtdcPromptTypeType(Enum):
    """日历提示类型类型"""
    SHFE_FTDC_CPT_Instrument = 49
    """合约上下市"""
    SHFE_FTDC_CPT_Margin = 50
    """保证金分段生效"""
    SHFE_FTDC_CPT_NULL = 0


class TShfeFtdcHasTrusteeType(Enum):
    """是否有托管人类型"""
    SHFE_FTDC_HT_Yes = 49
    """有"""
    SHFE_FTDC_HT_No = 48
    """没有"""
    SHFE_FTDC_HT_NULL = 0


class TShfeFtdcAmTypeType(Enum):
    """机构类型类型"""
    SHFE_FTDC_AMT_Bank = 49
    """银行"""
    SHFE_FTDC_AMT_Securities = 50
    """证券公司"""
    SHFE_FTDC_AMT_Fund = 51
    """基金公司"""
    SHFE_FTDC_AMT_Insurance = 52
    """保险公司"""
    SHFE_FTDC_AMT_Trust = 53
    """信托公司"""
    SHFE_FTDC_AMT_Other = 57
    """其他"""
    SHFE_FTDC_AMT_NULL = 0


class TShfeFtdcCSRCFundIOTypeType(Enum):
    """出入金类型类型"""
    SHFE_FTDC_CFIOT_FundIO = 48
    """出入金"""
    SHFE_FTDC_CFIOT_SwapCurrency = 49
    """银期换汇"""
    SHFE_FTDC_CFIOT_NULL = 0


class TShfeFtdcCusAccountTypeType(Enum):
    """结算账户类型类型"""
    SHFE_FTDC_CAT_Futures = 49
    """期货结算账户"""
    SHFE_FTDC_CAT_AssetmgrFuture = 50
    """纯期货资管业务下的资管结算账户"""
    SHFE_FTDC_CAT_AssetmgrTrustee = 51
    """综合类资管业务下的期货资管托管账户"""
    SHFE_FTDC_CAT_AssetmgrTransfer = 52
    """综合类资管业务下的资金中转账户"""
    SHFE_FTDC_CAT_NULL = 0


class TShfeFtdcLanguageTypeType(Enum):
    """通知语言类型类型"""
    SHFE_FTDC_LT_Chinese = 49
    """中文"""
    SHFE_FTDC_LT_English = 50
    """英文"""
    SHFE_FTDC_LT_NULL = 0


class TShfeFtdcAssetmgrClientTypeType(Enum):
    """资产管理客户类型类型"""
    SHFE_FTDC_AMCT_Person = 49
    """个人资管客户"""
    SHFE_FTDC_AMCT_Organ = 50
    """单位资管客户"""
    SHFE_FTDC_AMCT_SpecialOrgan = 52
    """特殊单位资管客户"""
    SHFE_FTDC_AMCT_NULL = 0


class TShfeFtdcAssetmgrTypeType(Enum):
    """投资类型类型"""
    SHFE_FTDC_ASST_Futures = 51
    """期货类"""
    SHFE_FTDC_ASST_SpecialOrgan = 52
    """综合类"""
    SHFE_FTDC_ASST_NULL = 0


class TShfeFtdcCheckInstrTypeType(Enum):
    """合约比较类型类型"""
    SHFE_FTDC_CIT_HasExch = 48
    """合约交易所不存在"""
    SHFE_FTDC_CIT_HasATP = 49
    """合约本系统不存在"""
    SHFE_FTDC_CIT_HasDiff = 50
    """合约比较不一致"""
    SHFE_FTDC_CIT_NULL = 0


class TShfeFtdcDeliveryTypeType(Enum):
    """交割类型类型"""
    SHFE_FTDC_DT_HandDeliv = 49
    """手工交割"""
    SHFE_FTDC_DT_PersonDeliv = 50
    """到期交割"""
    SHFE_FTDC_DT_NULL = 0


class TShfeFtdcMaxMarginSideAlgorithmType(Enum):
    """大额单边保证金算法类型"""
    SHFE_FTDC_MMSA_NO = 48
    """不使用大额单边保证金算法"""
    SHFE_FTDC_MMSA_YES = 49
    """使用大额单边保证金算法"""
    SHFE_FTDC_MMSA_NULL = 0


class TShfeFtdcDAClientTypeType(Enum):
    """资产管理客户类型类型"""
    SHFE_FTDC_CACT_Person = 48
    """自然人"""
    SHFE_FTDC_CACT_Company = 49
    """法人"""
    SHFE_FTDC_CACT_Other = 50
    """其他"""
    SHFE_FTDC_CACT_NULL = 0


class TShfeFtdcUOAAssetmgrTypeType(Enum):
    """投资类型类型"""
    SHFE_FTDC_UOAAT_Futures = 49
    """期货类"""
    SHFE_FTDC_UOAAT_SpecialOrgan = 50
    """综合类"""
    SHFE_FTDC_UOAAT_NULL = 0


class TShfeFtdcDirectionEnType(Enum):
    """买卖方向类型"""
    SHFE_FTDC_DEN_Buy = 48
    """Buy"""
    SHFE_FTDC_DEN_Sell = 49
    """Sell"""
    SHFE_FTDC_DEN_NULL = 0


class TShfeFtdcOffsetFlagEnType(Enum):
    """开平标志类型"""
    SHFE_FTDC_OFEN_Open = 48
    """Position Opening"""
    SHFE_FTDC_OFEN_Close = 49
    """Position Close"""
    SHFE_FTDC_OFEN_ForceClose = 50
    """Forced Liquidation"""
    SHFE_FTDC_OFEN_CloseToday = 51
    """Close Today"""
    SHFE_FTDC_OFEN_CloseYesterday = 52
    """Close Prev."""
    SHFE_FTDC_OFEN_ForceOff = 53
    """Forced Reduction"""
    SHFE_FTDC_OFEN_LocalForceClose = 54
    """Local Forced Liquidation"""
    SHFE_FTDC_OFEN_NULL = 0


class TShfeFtdcHedgeFlagEnType(Enum):
    """投机套保标志类型"""
    SHFE_FTDC_HFEN_Speculation = 49
    """Speculation"""
    SHFE_FTDC_HFEN_Arbitrage = 50
    """Arbitrage"""
    SHFE_FTDC_HFEN_Hedge = 51
    """Hedge"""
    SHFE_FTDC_HFEN_NULL = 0


class TShfeFtdcFundIOTypeEnType(Enum):
    """出入金类型类型"""
    SHFE_FTDC_FIOTEN_FundIO = 49
    """Deposit/Withdrawal"""
    SHFE_FTDC_FIOTEN_Transfer = 50
    """Bank-Futures Transfer"""
    SHFE_FTDC_FIOTEN_SwapCurrency = 51
    """Bank-Futures FX Exchange"""
    SHFE_FTDC_FIOTEN_NULL = 0


class TShfeFtdcFundTypeEnType(Enum):
    """资金类型类型"""
    SHFE_FTDC_FTEN_Deposite = 49
    """Bank Deposit"""
    SHFE_FTDC_FTEN_ItemFund = 50
    """Payment/Fee"""
    SHFE_FTDC_FTEN_Company = 51
    """Brokerage Adj"""
    SHFE_FTDC_FTEN_InnerTransfer = 52
    """Internal Transfer"""
    SHFE_FTDC_FTEN_NULL = 0


class TShfeFtdcFundDirectionEnType(Enum):
    """出入金方向类型"""
    SHFE_FTDC_FDEN_In = 49
    """Deposit"""
    SHFE_FTDC_FDEN_Out = 50
    """Withdrawal"""
    SHFE_FTDC_FDEN_NULL = 0


class TShfeFtdcFundMortDirectionEnType(Enum):
    """货币质押方向类型"""
    SHFE_FTDC_FMDEN_In = 49
    """Pledge"""
    SHFE_FTDC_FMDEN_Out = 50
    """Redemption"""
    SHFE_FTDC_FMDEN_NULL = 0


class TShfeFtdcOptionsTypeType(Enum):
    """期权类型类型"""
    SHFE_FTDC_CP_CallOptions = 49
    """看涨"""
    SHFE_FTDC_CP_PutOptions = 50
    """看跌"""
    SHFE_FTDC_CP_NULL = 0
    SHFE_FTDC_CP_NotOptions2 = 48 # 增加
    """非期权"""


class TShfeFtdcStrikeModeType(Enum):
    """执行方式类型"""
    SHFE_FTDC_STM_Continental = 48
    """欧式"""
    SHFE_FTDC_STM_American = 49
    """美式"""
    SHFE_FTDC_STM_Bermuda = 50
    """百慕大"""
    SHFE_FTDC_STM_NULL = 0


class TShfeFtdcStrikeTypeType(Enum):
    """执行类型类型"""
    SHFE_FTDC_STT_Hedge = 48
    """自身对冲"""
    SHFE_FTDC_STT_Match = 49
    """匹配执行"""
    SHFE_FTDC_STT_NULL = 0


class TShfeFtdcApplyTypeType(Enum):
    """中金所期权放弃执行申请类型类型"""
    SHFE_FTDC_APPT_NotStrikeNum = 52
    """不执行数量"""
    SHFE_FTDC_APPT_NULL = 0


class TShfeFtdcGiveUpDataSourceType(Enum):
    """放弃执行申请数据来源类型"""
    SHFE_FTDC_GUDS_Gen = 48
    """系统生成"""
    SHFE_FTDC_GUDS_Hand = 49
    """手工添加"""
    SHFE_FTDC_GUDS_NULL = 0


class TShfeFtdcExecResultType(Enum):
    """执行结果类型"""
    SHFE_FTDC_OER_NoExec = 110
    """没有执行"""
    SHFE_FTDC_OER_Canceled = 99
    """已经取消"""
    SHFE_FTDC_OER_OK = 48
    """执行成功"""
    SHFE_FTDC_OER_NoPosition = 49
    """期权持仓不够"""
    SHFE_FTDC_OER_NoDeposit = 50
    """资金不够"""
    SHFE_FTDC_OER_NoParticipant = 51
    """会员不存在"""
    SHFE_FTDC_OER_NoClient = 52
    """客户不存在"""
    SHFE_FTDC_OER_NoInstrument = 54
    """合约不存在"""
    SHFE_FTDC_OER_NoRight = 55
    """没有执行权限"""
    SHFE_FTDC_OER_InvalidVolume = 56
    """不合理的数量"""
    SHFE_FTDC_OER_NoEnoughHistoryTrade = 57
    """没有足够的历史成交"""
    SHFE_FTDC_OER_Unknown = 97
    """未知"""
    SHFE_FTDC_OER_NULL = 0


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


class TShfeFtdcOptionRoyaltyPriceTypeType(Enum):
    """期权权利金价格类型类型"""
    SHFE_FTDC_ORPT_PreSettlementPrice = 49
    """昨结算价"""
    SHFE_FTDC_ORPT_OpenPrice = 52
    """开仓价"""
    SHFE_FTDC_ORPT_MaxPreSettlementPrice = 53
    """最新价与昨结算价较大值"""
    SHFE_FTDC_ORPT_NULL = 0


class TShfeFtdcBalanceAlgorithmType(Enum):
    """权益算法类型"""
    SHFE_FTDC_BLAG_Default = 49
    """不计算期权市值盈亏"""
    SHFE_FTDC_BLAG_IncludeOptValLost = 50
    """计算期权市值亏损"""
    SHFE_FTDC_BLAG_NULL = 0


class TShfeFtdcActionTypeType(Enum):
    """执行类型类型"""
    SHFE_FTDC_ACTP_Exec = 49
    """执行"""
    SHFE_FTDC_ACTP_Abandon = 50
    """放弃"""
    SHFE_FTDC_ACTP_NULL = 0


class TShfeFtdcForQuoteStatusType(Enum):
    """询价状态类型"""
    SHFE_FTDC_FQST_Submitted = 97
    """已经提交"""
    SHFE_FTDC_FQST_Accepted = 98
    """已经接受"""
    SHFE_FTDC_FQST_Rejected = 99
    """已经被拒绝"""
    SHFE_FTDC_FQST_NULL = 0


class TShfeFtdcValueMethodType(Enum):
    """取值方式类型"""
    SHFE_FTDC_VM_Absolute = 48
    """按绝对值"""
    SHFE_FTDC_VM_Ratio = 49
    """按比率"""
    SHFE_FTDC_VM_NULL = 0


class TShfeFtdcExecOrderPositionFlagType(Enum):
    """期权行权后是否保留期货头寸的标记类型"""
    SHFE_FTDC_EOPF_Reserve = 48
    """保留"""
    SHFE_FTDC_EOPF_UnReserve = 49
    """不保留"""
    SHFE_FTDC_EOPF_NULL = 0


class TShfeFtdcExecOrderCloseFlagType(Enum):
    """期权行权后生成的头寸是否自动平仓类型"""
    SHFE_FTDC_EOCF_AutoClose = 48
    """自动平仓"""
    SHFE_FTDC_EOCF_NotToClose = 49
    """免于自动平仓"""
    SHFE_FTDC_EOCF_NULL = 0


class TShfeFtdcProductTypeType(Enum):
    """产品类型类型"""
    SHFE_FTDC_PTE_Futures = 49
    """期货"""
    SHFE_FTDC_PTE_Options = 50
    """期权"""
    SHFE_FTDC_PTE_NULL = 0


class TShfeFtdcCZCEUploadFileNameType(Enum):
    """郑商所结算文件名类型"""
    SHFE_FTDC_CUFN_CUFN_O = 79
    """^\d{8}_zz_\d{4}"""
    SHFE_FTDC_CUFN_CUFN_T = 84
    """^\d{8}成交表"""
    SHFE_FTDC_CUFN_CUFN_P = 80
    """^\d{8}单腿持仓表new"""
    SHFE_FTDC_CUFN_CUFN_N = 78
    """^\d{8}非平仓了结表"""
    SHFE_FTDC_CUFN_CUFN_L = 76
    """^\d{8}平仓表"""
    SHFE_FTDC_CUFN_CUFN_F = 70
    """^\d{8}资金表"""
    SHFE_FTDC_CUFN_CUFN_C = 67
    """^\d{8}组合持仓表"""
    SHFE_FTDC_CUFN_CUFN_M = 77
    """^\d{8}保证金参数表"""
    SHFE_FTDC_CUFN_NULL = 0


class TShfeFtdcDCEUploadFileNameType(Enum):
    """大商所结算文件名类型"""
    SHFE_FTDC_DUFN_DUFN_O = 79
    """^\d{8}_dl_\d{3}"""
    SHFE_FTDC_DUFN_DUFN_T = 84
    """^\d{8}_成交表"""
    SHFE_FTDC_DUFN_DUFN_P = 80
    """^\d{8}_持仓表"""
    SHFE_FTDC_DUFN_DUFN_F = 70
    """^\d{8}_资金结算表"""
    SHFE_FTDC_DUFN_DUFN_C = 67
    """^\d{8}_优惠组合持仓明细表"""
    SHFE_FTDC_DUFN_DUFN_D = 68
    """^\d{8}_持仓明细表"""
    SHFE_FTDC_DUFN_DUFN_M = 77
    """^\d{8}_保证金参数表"""
    SHFE_FTDC_DUFN_DUFN_S = 83
    """^\d{8}_期权执行表"""
    SHFE_FTDC_DUFN_NULL = 0


class TShfeFtdcSHFEUploadFileNameType(Enum):
    """上期所结算文件名类型"""
    SHFE_FTDC_SUFN_SUFN_O = 79
    """^\d{4}_\d{8}_\d{8}_DailyFundChg"""
    SHFE_FTDC_SUFN_SUFN_T = 84
    """^\d{4}_\d{8}_\d{8}_Trade"""
    SHFE_FTDC_SUFN_SUFN_P = 80
    """^\d{4}_\d{8}_\d{8}_SettlementDetail"""
    SHFE_FTDC_SUFN_SUFN_F = 70
    """^\d{4}_\d{8}_\d{8}_Capital"""
    SHFE_FTDC_SUFN_NULL = 0


class TShfeFtdcCFFEXUploadFileNameType(Enum):
    """中金所结算文件名类型"""
    SHFE_FTDC_CFUFN_SUFN_T = 84
    """^\d{4}_SG\d{1}_\d{8}_\d{1}_Trade"""
    SHFE_FTDC_CFUFN_SUFN_P = 80
    """^\d{4}_SG\d{1}_\d{8}_\d{1}_SettlementDetail"""
    SHFE_FTDC_CFUFN_SUFN_F = 70
    """^\d{4}_SG\d{1}_\d{8}_\d{1}_Capital"""
    SHFE_FTDC_CFUFN_SUFN_S = 83
    """^\d{4}_SG\d{1}_\d{8}_\d{1}_OptionExec"""
    SHFE_FTDC_CFUFN_NULL = 0


class TShfeFtdcCombDirectionType(Enum):
    """组合指令方向类型"""
    SHFE_FTDC_CMDR_Comb = 48
    """申请组合"""
    SHFE_FTDC_CMDR_UnComb = 49
    """申请拆分"""
    SHFE_FTDC_CMDR_NULL = 0


class TShfeFtdcStrikeOffsetTypeType(Enum):
    """行权偏移类型类型"""
    SHFE_FTDC_STOV_RealValue = 49
    """实值额"""
    SHFE_FTDC_STOV_ProfitValue = 50
    """盈利额"""
    SHFE_FTDC_STOV_RealRatio = 51
    """实值比例"""
    SHFE_FTDC_STOV_ProfitRatio = 52
    """盈利比例"""
    SHFE_FTDC_STOV_NULL = 0


class TShfeFtdcReserveOpenAccStasType(Enum):
    """预约开户状态类型"""
    SHFE_FTDC_ROAST_Processing = 48
    """等待处理中"""
    SHFE_FTDC_ROAST_Cancelled = 49
    """已撤销"""
    SHFE_FTDC_ROAST_Opened = 50
    """已开户"""
    SHFE_FTDC_ROAST_Invalid = 51
    """无效请求"""
    SHFE_FTDC_ROAST_NULL = 0


class TShfeFtdcNewsUrgencyType(Enum):
    """紧急程度类型"""


class TShfeFtdcWeakPasswordSourceType(Enum):
    """弱密码来源类型"""
    SHFE_FTDC_WPSR_Lib = 49
    """弱密码库"""
    SHFE_FTDC_WPSR_Manual = 50
    """手工录入"""
    SHFE_FTDC_WPSR_NULL = 0


class TShfeFtdcOptSelfCloseFlagType(Enum):
    """期权行权的头寸是否自对冲类型"""
    SHFE_FTDC_OSCF_CloseSelfOptionPosition = 49
    """自对冲期权仓位"""
    SHFE_FTDC_OSCF_ReserveOptionPosition = 50
    """保留期权仓位"""
    SHFE_FTDC_OSCF_SellCloseSelfFuturePosition = 51
    """自对冲卖方履约后的期货仓位"""
    SHFE_FTDC_OSCF_NULL = 0


class TShfeFtdcBizTypeType(Enum):
    """业务类型类型"""
    SHFE_FTDC_BZTP_Future = 49
    """期货"""
    SHFE_FTDC_BZTP_Stock = 50
    """证券"""
    SHFE_FTDC_BZTP_NULL = 0


class TShfeFtdcMD5Type(Enum):
    """MD5校验码类型"""
    SHFE_FTDC_MD5_NULL = 0 # 增加

class TShfeFtdcAccountSortTypeType(Enum):
    """资金排序方法类型"""
    SHFE_FTDC_ACTST_NA = 49
    """不排序"""
    SHFE_FTDC_ACTST_Balance = 50
    """按总权益排序"""
    SHFE_FTDC_ACTST_Available = 51
    """按可用资金排序"""
    SHFE_FTDC_ACTST_CurrMargin = 52
    """按保证金排序"""
    SHFE_FTDC_ACTST_Risk = 53
    """按风险度排序"""
    SHFE_FTDC_ACTST_NULL = 0


class TShfeFtdcPositionSortTypeType(Enum):
    """持仓排序方法类型"""
    SHFE_FTDC_PSTST_NA = 49
    """不排序"""
    SHFE_FTDC_PSTST_TotolPosition = 50
    """按总持仓排序"""
    SHFE_FTDC_PSTST_LongPosition = 51
    """按多头持仓排序"""
    SHFE_FTDC_PSTST_ShortPosition = 52
    """按空头持仓排序"""
    SHFE_FTDC_PSTST_NetPosition = 53
    """按净持仓排序"""
    SHFE_FTDC_PSTST_NULL = 0


class TShfeFtdcTradeSortTypeType(Enum):
    """交易排序方法类型"""
    SHFE_FTDC_TRDST_NA = 49
    """不排序"""
    SHFE_FTDC_TRDST_TotolTradeVolume = 50
    """按总成交量排序"""
    SHFE_FTDC_TRDST_TotolTrade = 51
    """按总成交额排序"""
    SHFE_FTDC_TRDST_LongPositionTrade = 52
    """按多头成交量排序"""
    SHFE_FTDC_TRDST_ShortPositionTrade = 53
    """按空头成交量排序"""
    SHFE_FTDC_TRDST_NetPositionTrade = 54
    """按净成交量排序"""
    SHFE_FTDC_TRDST_NULL = 0


class TShfeFtdcStatSortTypeType(Enum):
    """stat sort type类型"""
    SHFE_FTDC_SST_NA = 49
    """do not sort"""
    SHFE_FTDC_SST_TotolVolume = 50
    """sort by total volume(position,trade,order)"""
    SHFE_FTDC_SST_TotolAmount = 51
    """sort by total amount(trade)"""
    SHFE_FTDC_SST_LongVolume = 52
    """sort by long volume(position,trade,order)"""
    SHFE_FTDC_SST_ShortVolume = 53
    """sort by short volume(position,trade,order)"""
    SHFE_FTDC_SST_NetVolume = 54
    """sort by net volume(position,trade,order)"""
    SHFE_FTDC_SST_NULL = 0


class TShfeFtdcValueModeType(Enum):
    """取值方式类型"""
    SHFE_FTDC_VMD_None = 48
    """无"""
    SHFE_FTDC_VMD_Percentage = 49
    """百分比"""
    SHFE_FTDC_VMD_Absolute = 50
    """绝对值"""
    SHFE_FTDC_VMD_NULL = 0


class TShfeFtdcSTPriceTypeType(Enum):
    """压力测试结算价类型类型"""
    SHFE_FTDC_STPT_CustomPrice = 49
    """自定义价格"""
    SHFE_FTDC_STPT_LatestPrice = 50
    """最新价"""
    SHFE_FTDC_STPT_AveragePrice = 51
    """成交均价"""
    SHFE_FTDC_STPT_UpperLimitPrice = 52
    """涨停板价"""
    SHFE_FTDC_STPT_LowerLimitPrice = 53
    """跌停板价"""
    SHFE_FTDC_STPT_NULL = 0


class TShfeFtdcNotifyTimeType(Enum):
    """风险通知时间类型"""
    SHFE_FTDC_NT_Trading = 48
    """盘中"""
    SHFE_FTDC_NT_Closed = 49
    """盘后"""
    SHFE_FTDC_NT_NULL = 0


class TShfeFtdcForceCloseLevelType(Enum):
    """强平标准类型"""
    SHFE_FTDC_FCL_BrokerLevel = 48
    """经纪公司标准"""
    SHFE_FTDC_FCL_ExchangeLevel = 49
    """交易所标准"""
    SHFE_FTDC_FCL_NULL = 0


class TShfeFtdcForceCloseReleaseType(Enum):
    """强平资金释放标准类型"""
    SHFE_FTDC_FCR_RealTime = 48
    """实时结算标准"""
    SHFE_FTDC_FCR_LastSettlement = 49
    """以昨结算为标准"""
    SHFE_FTDC_FCR_StressTest = 50
    """以压力测试资金正常为标准"""
    SHFE_FTDC_FCR_NULL = 0


class TShfeFtdcFCRulePriorityItemType(Enum):
    """批量强平计算规则优先级项类型"""
    SHFE_FTDC_FCRPI_Direction = 48
    """持仓方向"""
    SHFE_FTDC_FCRPI_HedgeFlag = 49
    """投机套保"""
    SHFE_FTDC_FCRPI_PosiDate = 50
    """持仓日期"""
    SHFE_FTDC_FCRPI_NULL = 0


class TShfeFtdcForceClosePosiDirectionType(Enum):
    """强平持仓方向类型"""
    SHFE_FTDC_FCPD_NA = 48
    """未定义"""
    SHFE_FTDC_FCPD_LongShort = 49
    """先多头后空头"""
    SHFE_FTDC_FCPD_ShortLong = 50
    """先空头后多头"""
    SHFE_FTDC_FCPD_Long = 51
    """只平多头持仓"""
    SHFE_FTDC_FCPD_Short = 52
    """只平空头持仓"""
    SHFE_FTDC_FCPD_LargeMargin = 53
    """先平占用保证金多的方向持仓"""
    SHFE_FTDC_FCPD_SmallMargin = 54
    """先平占用保证金少的方向持仓"""
    SHFE_FTDC_FCPD_NULL = 0


class TShfeFtdcForceCloseHedgeFlagType(Enum):
    """强平投机套保标志类型"""
    SHFE_FTDC_FCHF_NA = 48
    """未定义"""
    SHFE_FTDC_FCHF_SpeculationHedge = 49
    """先投机后套保"""
    SHFE_FTDC_FCHF_Speculation = 50
    """只平投机"""
    SHFE_FTDC_FCHF_NULL = 0


class TShfeFtdcForceCloseCombPosiFlagType(Enum):
    """强平组合持仓标志类型"""
    SHFE_FTDC_FCCPF_NA = 48
    """未定义"""
    SHFE_FTDC_FCCPF_ExcludeComb = 49
    """不包含组合持仓"""
    SHFE_FTDC_FCCPF_IncludeComb = 50
    """包含组合持仓"""
    SHFE_FTDC_FCCPF_NULL = 0


class TShfeFtdcForceCloseHistoryPosiOrderType(Enum):
    """强平历史持仓顺序类型"""
    SHFE_FTDC_FCHPO_NA = 48
    """未定义"""
    SHFE_FTDC_FCHPO_HistoryFirst = 49
    """先平历史持仓"""
    SHFE_FTDC_FCHPO_TodayFirst = 50
    """先平今持仓"""
    SHFE_FTDC_FCHPO_NULL = 0


class TShfeFtdcForceClosePriceTypeType(Enum):
    """强平价格类型类型"""
    SHFE_FTDC_FCPT_StopPrice = 48
    """反向涨跌停"""
    SHFE_FTDC_FCPT_LimitPrice = 49
    """限价"""
    SHFE_FTDC_FCPT_MarketFirst = 50
    """市价"""
    SHFE_FTDC_FCPT_NULL = 0


class TShfeFtdcPriceVaryDirType(Enum):
    """价格波动方向类型"""
    SHFE_FTDC_PVD_Up = 48
    """上涨"""
    SHFE_FTDC_PVD_Down = 49
    """下跌"""
    SHFE_FTDC_PVD_None = 50
    """无涨跌"""
    SHFE_FTDC_PVD_NULL = 0


class TShfeFtdcPriceVaryAlgoType(Enum):
    """合约价格波动方法类型"""
    SHFE_FTDC_PVA_Equal = 48
    """所有合约相同幅度波动"""
    SHFE_FTDC_PVA_Sequence = 49
    """按合约接收到先后顺序"""
    SHFE_FTDC_PVA_NULL = 0


class TShfeFtdcPriceTypeType(Enum):
    """基本的价格类型类型"""
    SHFE_FTDC_BPT_LastSettlement = 49
    """昨结算价"""
    SHFE_FTDC_BPT_LaseClose = 50
    """昨收盘价"""
    SHFE_FTDC_BPT_Settlement = 51
    """结算价"""
    SHFE_FTDC_BPT_Average = 52
    """成交均价"""
    SHFE_FTDC_BPT_Open = 53
    """开仓价"""
    SHFE_FTDC_BPT_Latest = 54
    """最新价"""
    SHFE_FTDC_BPT_UpperLimit = 55
    """涨停板价"""
    SHFE_FTDC_BPT_LowerLimit = 56
    """跌停板价"""
    SHFE_FTDC_BPT_Customize = 57
    """指定价格"""
    SHFE_FTDC_BPT_NULL = 0


class TShfeFtdcOrderTriggerTypeType(Enum):
    """预埋单触发类型类型"""
    SHFE_FTDC_OTT_Customize = 49
    """用户指定时间"""
    SHFE_FTDC_OTT_TradeSegment = 50
    """交易阶段"""
    SHFE_FTDC_OTT_NULL = 0


class TShfeFtdcRiskUserTypeType(Enum):
    """风控用户类型 类型"""
    SHFE_FTDC_RUT_SuperUser = 48
    """管理员"""
    SHFE_FTDC_RUT_NULL = 0


class TShfeFtdcRiskParkedOrderStatusType(Enum):
    """风控预埋单状态类型"""
    SHFE_FTDC_RPOS_NotSend = 49
    """未发送"""
    SHFE_FTDC_RPOS_Send = 50
    """已发送"""
    SHFE_FTDC_RPOS_Deleted = 51
    """已删除"""
    SHFE_FTDC_RPOS_NULL = 0


class TShfeFtdcFrontTypeType(Enum):
    """前置类型类型"""
    SHFE_FTDC_RFT_NA = 48
    """未定义"""
    SHFE_FTDC_RFT_Riskfront = 49
    """风控前置"""
    SHFE_FTDC_RFT_Riskmonfnt = 50
    """监控前置"""
    SHFE_FTDC_RFT_Localfront = 51
    """本地前置"""
    SHFE_FTDC_RFT_NULL = 0


class TShfeFtdcSmsCustomTypeType(Enum):
    """短信类型类型"""
    SHFE_FTDC_SCT_RiskNotify = 48
    """风险通知"""
    SHFE_FTDC_SCT_BizNotify = 49
    """业务通知"""
    SHFE_FTDC_SCT_NULL = 0


class TShfeFtdcSTDCECombTypeType(Enum):
    """风控大商所组合类型类型"""
    SHFE_FTDC_RDCT_LOCK = 48
    """对锁"""
    SHFE_FTDC_RDCT_SP = 49
    """夸期"""
    SHFE_FTDC_RDCT_SPC = 50
    """夸品种"""
    SHFE_FTDC_RDCT_NULL = 0


class TShfeFtdcDailyNoticeTypeType(Enum):
    """每日通知类型类型"""
    SHFE_FTDC_DNT_NA = 48
    """未定义"""
    SHFE_FTDC_DNT_InstAdj = 49
    """5日内合约调整"""
    SHFE_FTDC_DNT_InstExpire = 50
    """5日内合约到期"""
    SHFE_FTDC_DNT_ExecAssigned = 51
    """指派行权"""
    SHFE_FTDC_DNT_CoveredComple = 52
    """备兑持仓标的数量补足"""
    SHFE_FTDC_DNT_NULL = 0


class TShfeFtdcLoginStatTypeType(Enum):
    """交易用户登录统计类型类型"""
    SHFE_FTDC_RLST_ByUser = 48
    """按同一用户统计"""
    SHFE_FTDC_RLST_ByAddress = 49
    """按同一IPMAC地址统计"""
    SHFE_FTDC_RLST_NULL = 0


