import { NgModule } from '@angular/core';
import { IonicApp, IonicModule } from 'ionic-angular';
import { MyApp } from './app.component';
import { AboutPage } from '../pages/about/about';
import { HomePage } from '../pages/home/home';
import { TabsPage } from '../pages/tabs/tabs';
import { DonatePage } from '../pages/donate/donate'
import { ChartModule } from 'ng2-chartjs2';
import { LoginPage } from '../pages/login-page/login-page'
import { CompanyPage} from '../pages/company-page/company-page'

@NgModule({
  declarations: [
    MyApp,
    AboutPage,
    HomePage,
    DonatePage,
    TabsPage,
    LoginPage,
    CompanyPage 
  ],
  imports: [
    IonicModule.forRoot(MyApp),
    ChartModule
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    AboutPage,
    DonatePage,
    HomePage,
    TabsPage,
    LoginPage,
    CompanyPage
  ],
  providers: []
})
export class AppModule {}
