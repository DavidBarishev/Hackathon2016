import { Component } from '@angular/core';
import { BarcodeScanner } from 'ionic-native';
import { NavController,NavParams } from 'ionic-angular';
import { APIService } from '../../providers/donation-service'

@Component({
  selector: 'page-about',
  templateUrl: 'about.html'
})
export class AboutPage {


  id:string;
  constructor(public donationService: APIService,public params:NavParams) {
    this.id = params.get('id');
  }

  beginDonate() : void {
    BarcodeScanner.scan().then((barcodeData) => { 
       console.log(barcodeData.text);
       let barcodTxt:String = barcodeData.text;
       if(barcodTxt.startsWith(''))

       this.donationService.startCharity(this.id);

    }, (err) => {
       alert(err);
    });
  } 

}
