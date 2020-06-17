var screening_center = [
    {
        "Name": "서귀포의료원",
        "adress": "제주특별자치도 서귀포시 장수로 47",
        "phonenumber": "064-730-3000"
    }, {
        "Name": "서귀포열린병원",
        "adress": "제주특별자치도 서귀포시 일주동로 8638 (동홍동)",
        "phonenumber": "064-762-8001"
	},  {
        "Name": "제주한라병원",
        "adress": "제주특별자치도 제주시 도령로 65 (연동, (연동))",
        "phonenumber": "064-740-5975"
	},  {
        "Name": "한마음병원",
        "adress": "제주특별자치도 제주시 연신로 52 (이도이동,(이도이동))",
        "phonenumber": "064-750-9119"
	},  {
        "Name": "한국병원",
        "adress": "제주특별자치도 제주시 서광로 193 (삼도일동, (삼도일동))",
        "phonenumber": "064-750-0119"
	}, {
        "Name": "중앙병원",
        "adress": "제주특별자치도 제주시 월랑로 91-0 (이호이동,중앙병원)",
        "phonenumber": "064-786-7000"
	}];


var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
        
        level: 6 // 지도의 확대 레벨 
    }; 

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
var geocoder = new kakao.maps.services.Geocoder();

$.getJSON('test.json', function(data) {
	for(var i = 0 ; i < data.count ; i++  ){
		var pharmacy= data.stores[i];
		if( pharmacy.remain_stat != 'break'){
			var message = pharmacy.name+"\n";
		    if( pharmacy.remain_stat == 'plenty')
                displayMarkerAdress(pharmacy.addr, message, "image/green.png" );
            else if( pharmacy.remain_stat == 'some')    
                displayMarkerAdress(pharmacy.addr, message, "image/yellow.png");
            else if( pharmacy.remain_stat == 'few')
                displayMarkerAdress(pharmacy.addr, message, "image/red.png");
            else if( pharmacy.remain_stat == 'empty')
                displayMarkerAdress(pharmacy.addr, message, "image/gray.png");
		}
        
	}
});

for(var i = 0 ; i < 6 ; i++  )
{	var center = screening_center[i];
 	var message = center["Name"]+"\n"+center["phonenumber"];
	displayMarkerAdress(center["adress"], message, "image/center.png");
}

// HTML5의 geolocation으로 사용할 수 있는지 확인합니다 
if (navigator.geolocation) {
    
    // GeoLocation을 이용해서 접속 위치를 얻어옵니다
    navigator.geolocation.getCurrentPosition(function(position) {
        
        var lat = position.coords.latitude, // 위도
            lon = position.coords.longitude; // 경도
      
        var locPosition = new kakao.maps.LatLng(lat, lon), // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
            message = "현위치" // 인포윈도우에 표시될 내용입니다
        
        // 마커와 인포윈도우를 표시합니다
        displayMarker(locPosition, message);
        map.setCenter(locPosition);  
		
      });
    
} else { // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다
    
    var locPosition = new kakao.maps.LatLng(33.450701, 126.570667),    
        message = 'geolocation을 사용할수 없어요..'
        
    displayMarker(locPosition, message);
}

	
// 지도에 마커와 인포윈도우를 표시하는 함수입니다
function displayMarker(locPosition, message) {
    
    var marker = new kakao.maps.Marker({  
        map: map, 
        position: locPosition,
		clickable: true
    }); 
    
    var iwContent = '<div style="padding:5px 20px 5px 5px; ">' + message + '</div>' // 인포윈도우에 표시할 내용
        iwRemoveable = true;

    // 인포윈도우를 생성합니다
    var infowindow = new kakao.maps.InfoWindow({
        content : iwContent,
        removable : iwRemoveable
    });
	
    kakao.maps.event.addListener(marker, 'click', function() {
      // 마커 위에 인포윈도우를 표시합니다
      infowindow.open(map, marker);  
	});
	if( message =='현위치' )
		infowindow.open(map, marker);  
}    

function displayMarker(locPosition, message, imageSrc) {
    imageSize = new kakao.maps.Size(50, 50), // 마커이미지의 크기입니다
    imageOption = {offset: new kakao.maps.Point(15, 15)};
    // 마커를 생성합니다
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);
        
    var marker = new kakao.maps.Marker({  
        map: map, 
        position: locPosition,
        image: markerImage,
		clickable: true
    }); 
    
    var iwContent = '<div style="padding:5px 20px 5px 5px; ">' + message + '</div>' // 인포윈도우에 표시할 내용
        iwRemoveable = true;

    // 인포윈도우를 생성합니다
    var infowindow = new kakao.maps.InfoWindow({
        content : iwContent,
        removable : iwRemoveable
    });
	
    kakao.maps.event.addListener(marker, 'click', function() {
      // 마커 위에 인포윈도우를 표시합니다
      infowindow.open(map, marker);  
	});
	if( message =='현위치' )
		infowindow.open(map, marker);  
}    


function displayMarkerAdress(adress, message) {
	geocoder.addressSearch(adress, function(result, status) {
    // 정상적으로 검색이 완료됐으면 
     if (status === kakao.maps.services.Status.OK) {
        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
		displayMarker(coords, message);
		 console.log("good");
	 } 
	else
		console.log(adress);
	});    
}  

function displayMarkerAdress(adress, message, imageSrc ) {
	geocoder.addressSearch(adress, function(result, status) {
    // 정상적으로 검색이 완료됐으면 
     if (status === kakao.maps.services.Status.OK) {
        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
		displayMarker(coords, message, imageSrc);
		 console.log("good");
	 } 
	else
		console.log(adress);
	});    
}  
	