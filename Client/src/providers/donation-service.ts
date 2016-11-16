import { Injectable } from '@angular/core';
import {Http, Headers, RequestOptions} from '@angular/http';
import 'rxjs/add/operator/map';

/*
  Generated class for the DonationService provider.

  See https://angular.io/docs/ts/latest/guide/dependency-injection.html
  for more info on providers and Angular 2 DI.
*/
@Injectable()
export class APIService {
  serverUrl:string = 'http://10.10.0.31:8080';
  httpClient: Http;

  constructor(public http: Http) {
    this.httpClient = http;
  }

  startCharity (id : string,companyID:string){
    let body = JSON.stringify({"user_id":id,"company_id":companyID});
    return new Promise(resolve => {
       this.http.post(this.serverUrl + '/api/start_vol',body)
        .map(res => res.json())
        .subscribe(data => {
            return resolve(data['success'] == true);
        });
    });
  }

  endCharity (id : string){
    let body = JSON.stringify({"user_id":id});
    return new Promise(resolve => {
       this.http.post(this.serverUrl + '/api/stop_vol',body)
        .map(res => res.json())
        .subscribe(data => {
            return resolve(data['success'] == true);
        });
    });
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

  alive(){
    return new Promise(resolve => {
    this.http.get(this.serverUrl)
      .map(res => res.json())
      .subscribe(data => {
        resolve(data);
      });
  });
  }

  login(id:string,password:string){
    let body = JSON.stringify({"user_id":id,"password":password});
    return new Promise(resolve => {
       this.http.post(this.serverUrl + '/api/login',body)
        .map(res => res.json())
        .subscribe(data => {
            return resolve(data['login'] == true);
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
