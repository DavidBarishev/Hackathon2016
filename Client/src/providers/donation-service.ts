import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

/*
  Generated class for the DonationService provider.

  See https://angular.io/docs/ts/latest/guide/dependency-injection.html
  for more info on providers and Angular 2 DI.
*/
@Injectable()
export class APIService {
  serverUrl:string = 'http://10.10.0.110:8080';
  httpClient: Http;

  constructor(public http: Http) {
    this.httpClient = http;
  }

  startCharity (id : string){
    let body = this.jsonToURLEncoded({"username":id});
    this.httpClient.post('/api/strat_vol',body)
  }

  endCharity (id : string){
    let body = this.jsonToURLEncoded({"username":id});
    this.httpClient.post(this.serverUrl + '/api/end_vol',body)
  }

  getInfo(id:string){
  return new Promise(resolve => {
    this.http.get(this.serverUrl + '/api/user_status/'+id)
      .map(res => res.json())
      .subscribe(data => {
        resolve(data);
      });
  });
  }

  login(id:string,password:string){
    let body = this.jsonToURLEncoded({"id":id,"password":password});
    return new Promise(resolve => {
       this.http.post(this.serverUrl + '/api/login',body)
        .map(res => res.json())
        .subscribe(data => {
            return resolve(data['suceess'] == true);
        });
    });
    
  }

  //convert a json object to the url encoded format of key=value&anotherkye=anothervalue
  private jsonToURLEncoded(jsonString){
    return Object.keys(jsonString).map(function(key){
      return encodeURIComponent(key) + '=' + encodeURIComponent(jsonString[key]);
    }).join('&');
  }

}
