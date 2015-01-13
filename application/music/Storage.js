//storage.js
// 首先创建一个helper方法连接数据库
function getDatabase() {
     return LocalStorage.openDatabaseSync("MusicList", "1.0", "StorageDatabase", 100000);
}

// 程序打开时，初始化表
function initialize() {
    var db = getDatabase();
    db.transaction(
        function(tx) {
            // 如果setting表不存在，则创建一个
            // 如果表存在，则跳过此步
            tx.executeSql('CREATE TABLE IF NOT EXISTS musiclist(id TEXT UNIQUE,title TEXT, time TEXT, source Text)');
      });
}

// 插入数据
function setMusic(id, title, time, source) {
   var db = getDatabase();
   var res = "";
   db.transaction(function(tx) {
        var rs = tx.executeSql('INSERT OR REPLACE INTO musiclist VALUES (?,?,?,?);', [id, title, time, source]);
              //console.log(rs.rowsAffected)
              if (rs.rowsAffected > 0) {
                res = "OK";
              } else {
                res = "Error";
              }
        }
  );
  return res;
}

 // 获取数据
function get(id) {
   var db = getDatabase();
   var res="";
   db.transaction(function(tx) {
     var rs = tx.executeSql('SELECT * FROM musiclist WHERE id=?;', [id]);
     if (rs.rows.length > 0) {
          res = rs.rows.item(0);
     } else {
         res = "Unknown";
     }
  })
  return res
}

function count(){
    var db = getDatabase();
    var c = 0;
    db.transaction(function(tx) {
      var rs = tx.executeSql('SELECT * FROM musiclist WHERE 1;');
      c = rs.rows.length;
   })
    return c;
}

function del(index){
    var db = getDatabase();
    var ret = 0;
    db.transaction(function(tx){
        ret = tx.executeSql('DELETE FROM musiclist WHERE id=?',index);
    })
    return ret;
}

function clear(){
    var db = getDatabase();
    var ret = 0;
    db.transaction(function(tx){
        ret = tx.executeSql('DELETE FROM musiclist WHERE 1');
    })
    return ret;
}
