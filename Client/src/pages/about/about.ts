import { Component } from '@angular/core';
import { BarcodeScanner } from 'ionic-native';
import { NavController,NavParams } from 'ionic-angular';
import { APIService } from '../../providers/donation-service'

@Component({
  selector: 'page-about',
  templateUrl: 'about.html',
  providers: [APIService]
})
export class AboutPage {


  id:string;
  constructor(public donationService: APIService,public params:NavParams) {
    this.id = params.get('id');
  }

  beginDonate() : void {
    BarcodeScanner.scan().then((barcodeData) => { 
       console.log(barcodeData.text);
       let barcodTxt:string = barcodeData.text;
       
       this.donationService.startCharity(this.id,barcodTxt)
        .then( res => {
              if (!res){
                alert('Error')
              }
              else{
                console.log('started vol');
              }
        });
    }, (err) => {
       alert(err);
    });
  } 

  stopDonate():void{
    BarcodeScanner.scan().then((barcodeData) => { 
       console.log(barcodeData.text);
       let barcodTxt:string = barcodeData.text;
       
       this.donationService.endCharity(this.id)
        .then( res => {
              if (!res){
                alert('Error')
              }
              else{
                console.log('stop vol');
              }
        });
    }, (err) => {
       alert(err);
    });
  }

}
