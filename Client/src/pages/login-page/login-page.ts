import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { APIService } from '../../providers/donation-service'
import {TabsPage} from '../tabs/tabs'
import {CompanyPage} from '../company-page/company-page'
/*
  Generated class for the LoginPage page.

  See http://ionicframework.com/docs/v2/components/#navigation for more info on
  Ionic pages and navigation.
*/
@Component({
  selector: 'page-login-page',
  templateUrl: 'login-page.html',
  providers: [APIService]
})
export class LoginPage {
  id: string;
  password: string;

  radioValue:string;

  constructor(public navCtrl: NavController, public apiService: APIService) { }

  login() {
    this.apiService.login(this.id, this.password)
      .then(result => {
        if (result) {
          if (this.radioValue == 'vol'){
            this.navCtrl.push(TabsPage,{"id":this.id});
          }
          else{
            this.navCtrl.push(CompanyPage,{"id":this.id});
          }
          
        }
        else{
          alert('Wrong Username/Password')
        }
      }

      )
  }

  dummylogin() {
    if (this.radioValue == 'vol'){
            this.navCtrl.push(TabsPage,{"id":this.id});
    }
    else{
            this.navCtrl.push(CompanyPage,{"id":this.id});
    }
  }

  alive(){
    this.apiService.alive()
     .then( res => {
       console.log(res);
       alert(res)
     })
  }

}
