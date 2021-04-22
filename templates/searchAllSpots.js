var local;
var resultArray= new Array();
var index;
function onSearchComplete(results) {
		var t = results.getNumPois();
		var totalPages = results.getNumPages();
        var currPage = results.getPageIndex();// 获取当前是第几页数据
		for(var j=0;j<results.getCurrentNumPois();j++)
		{
			resultArray[index]=results.getPoi(j);
			index = index+1;
		}
		if(results.getPageIndex()<results.getNumPages()-1)
			local.gotoPage(results.getPageIndex()+1);
	}
function searchAllSpots(address)//此为酒店的详细地址
{
	var map = new BMapGL.Map('container');
    map.centerAndZoom(new BMapGL.Point(116.331398,39.897445), 12);
    //创建地址解析器实例
    var myGeo = new BMapGL.Geocoder();
    // 将地址解析结果显示在地图上，并调整地图视野
    myGeo.getPoint(address, function(point){
    if(point){
        map.centerAndZoom(point, 11);
        map.addOverlay(new BMapGL.Marker(point, {title: address}));
		local = new BMapGL.LocalSearch(map, {renderOptions:{map: map},pageCapacity : 50});
		index=0;
		local.setSearchCompleteCallback(onSearchComplete);
		local.search("景点");
		map.enableScrollWheelZoom();
		}
		else{
            alert('您选择的地址没有解析到结果！');
			}
        }, '')
		return resultArray;
}
//searchAllSpots(addressOfHotel);