//输入起点和终点(结构化地址），返回两点间直线距离
var s;
function getDistance(lng1,lat1,lng2,lat2)
{
	var radlng1 = lng1*(Math.PI/180);
	var radlng2 = lng2*(Math.PI/180);
	var radlat1 = lat1*(Math.PI/180);
	var radlat2 = lat2*(Math.PI/180);
	var a = radlat1-radlat2;
	var b = radlng1-radlng2;
	var s = 2 * Math.asin(Math.sqrt(Math.pow(Math.sin(a/2),2) + Math.cos(radlat1)*Math.cos(radlat2)*Math.pow(Math.sin(b/2),2)));
	s = s*6378.137;
	s = Math.round(s*10)/10;
	return s;
}
function calculateDistance(address1,address2)
{
	var myGeo = new BMapGL.Geocoder();
	var lat1,lng1,lat2,lng2;
    myGeo.getPoint(address1, function(point){
    if(point){
		lat1 = point.lat;
		lng1 = point.lng;
		myGeo.getPoint(address2, function(point){
    if(point){
		lat2 = point.lat;
		lng2 = point.lng;
		s = getDistance(lng1,lat1,lng2,lat2);
		}
		else{
            alert('您选择的地址没有解析到结果！');
			}
        }, '')
		}
		else{
            alert('您选择的地址没有解析到结果！');
			}
        }, '')
	return s;
}