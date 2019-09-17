let _api = '/api'
export default {
    queryStationTempByPage: _api + '/StationBaseController/queryStationTempByPage', //查询实时数据
    queryStationTempByPageDateil: _api + '/StationBaseController/queryStationTempByPageDateil', //根据站点查询当天数据
    
    queryPlatform: _api + '/StationBaseController/queryPlatform', //查询所有管理中的平台
    queryStation: _api + '/StationBaseController/queryStation', //查询该平台下所有站点名称
    queryStationFialByPage: _api + '/StationBaseController/queryStationFialByPage', //查询历史数据

    addStationConfigWarning: _api + '/StationBaseController/addStationConfigWarning', //添加报警配置
    updateStationConfig: _api + '/StationBaseController/updateStationConfig', //修改报警配置
    queryStationConfigAll: _api + '/StationBaseController/queryStationConfigAll', //查询报警配置
    delStationConfig: _api + '/StationBaseController/delStationConfig', //删除报警配置
}