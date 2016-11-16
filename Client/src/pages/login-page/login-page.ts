import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { APIService } from '../../providers/donation-service'
import {TabsPage} from '../tabs/tabs'
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

  constructor(public navCtrl: NavController, public apiService: APIService) { }

  login() {
    this.apiService.login(this.id, this.password)
      .then(result => {
        if (result) {
          this.navCtrl.push(TabsPage)
        }
        else{
          alert('Wrong Username/Password')
        }
      }

      )
  }

  dummylogin() {
    console.log('Login: ' + this.id)
    this.navCtrl.push(TabsPage,{"id":this.id})
  }

}
