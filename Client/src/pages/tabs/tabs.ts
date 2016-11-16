import { Component, } from '@angular/core';
import { NavController,NavParams } from 'ionic-angular';

import { HomePage } from '../home/home';
import { AboutPage } from '../about/about';

@Component({
  templateUrl: 'tabs.html'
})
export class TabsPage {
  // this tells the tabs component which Pages
  // should be each tab's root Page
  tab1Root: any = HomePage;
  tab2Root: any = AboutPage;
  
  id:any;

  constructor(public navCtrl: NavController,public params:NavParams) {
    console.log('Tabs: '+params.get('id'))
    this.id = {'id':params.get('id')};
  }
}
