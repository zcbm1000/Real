        let days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];


        function getCurrentDate(){
            console.log('getCurrentDate CALLED')

        
        // 날짜 시간
        let today = new Date();
        console.log('today:', today);

        let year = today.getFullYear();    // 년(2026)
        let month = today.getMonth();      // 월(5, 0~11)
        let date = today.getDate();        // 일(16))
        let day = today.getDay();          // 요일(2, 0일 1월 2화)
    
        str +='[' + year + '/' + (month+1) + '/' + date + '/' + days[day] +']';
        // [2026/05/16/2]  실제로는 6월이나 1월부터 번호0으로 들어감,  2는 화요일을 뜻하나 숫자로표기됨 해당내용을 바꿈
        // [2026/06/16/화]
        return str;
        }