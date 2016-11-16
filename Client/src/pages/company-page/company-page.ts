import { Component } from '@angular/core';
import { NavController,NavParams } from 'ionic-angular';

/*
  Generated class for the CompanyPage page.

  See http://ionicframework.com/docs/v2/components/#navigation for more info on
  Ionic pages and navigation.
*/
@Component({
  selector: 'page-company-page',
  templateUrl: 'company-page.html'
})
export class CompanyPage {
   id:string;
  
   imgSource:string;


  constructor(public navCtrl: NavController,public params:NavParams) {
    alert(params)
    this.id = params.get('id');
    this.imgSource = 'http://www.expressmedia.org.au/wp-content/uploads/2016/01/white-page.jpg';
  }

  genCode(){
    this.imgSource = 'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data='+this.id;
  }





}
