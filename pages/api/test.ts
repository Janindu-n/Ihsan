$("button").click(function(){
        $.post("http://10.225.148.250/submitAI",
        {
            grid: [
                [
                  { is_person: true, health: 52, age: 68 },
                  { is_person: true, health: 9, age: 29 },
                  { is_person: false, health: 89, age: 98 },
                  { is_person: true, health: 17, age: 14 }
                ]
            ]
        },
        function(data: any, status: any){
            alert("Data: " + data + "\nStatus: " + status);
        });
    });
  