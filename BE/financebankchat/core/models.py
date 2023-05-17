from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class provider(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Trang cung cấp thông tin')
    alias = models.CharField(max_length=200, null=True, blank=True)
    

class stock(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=200, null=True, blank=True)

# Tài sản
class propertise(models.Model): 
    stock = models.ForeignKey(stock, null=False, on_delete=models.CASCADE)
    provider = models.ForeignKey(provider, null=False, on_delete=models.CASCADE, default='FBC')
    year = models.IntegerField(null=False, blank=False, default=datetime.now)
    cash  = models.FloatField(default=0, verbose_name='Tiền mặt, vàng, bạc')
    deposit = models.FloatField(default=0, verbose_name='Tiền gửi tại ngân hàng nhà nước')
    loan_credit_institutions = models.FloatField(default=0, verbose_name='Cho vay các tổ chức tín dụng')
    loan_customer = models.FloatField(default=0, verbose_name='Cho vay khách hàng')
    total = models.FloatField(default=0, verbose_name='Tổng tài sản')

    class Meta:
        ordering = ['stock']
        unique_together = [['stock', 'year', 'provider']]

# Nợ
class debt(models.Model):
    stock = models.ForeignKey(stock, null=False, on_delete=models.CASCADE)
    provider = models.ForeignKey(provider, null=False, on_delete=models.CASCADE, default='FBC')
    year = models.IntegerField(null=False, blank=False, default=datetime.now)
    bad_debt = models.FloatField(default=0, verbose_name='Nợ xấu')
    total_debt = models.FloatField(default=0, verbose_name='Dư nợ')
    class Meta:
        ordering = ['stock']
        unique_together = [['stock', 'year', 'provider']]


# Thu nhập
class income(models.Model):
    stock = models.ForeignKey(stock, null=False, on_delete=models.CASCADE)
    provider = models.ForeignKey(provider, null=False, on_delete=models.CASCADE, default='FBC')
    year = models.IntegerField(null=False, blank=False, default=datetime.now)
    net_interest_income= models.FloatField(default=0, verbose_name='Lãi thuần')
    interest_income= models.FloatField(default=0, verbose_name='Lãi')
    service_activities= models.FloatField(default=0, verbose_name='Lợi nhuận từ hoạt động dịch vụ')
    other_activities= models.FloatField(default=0, verbose_name='Lợi nhuận từ hoạt động khác')
    profit_after_tax= models.FloatField(default=0, verbose_name='Lợi nhuận sau thuế')
    class Meta:
        ordering = ['stock']
        unique_together = [['stock', 'year', 'provider']]


# Chỉ số
class index(models.Model):
    stock = models.ForeignKey(stock, null=False, on_delete=models.CASCADE)
    provider = models.ForeignKey(provider, null=False, on_delete=models.CASCADE, default='FBC')
    year = models.IntegerField(null=False, blank=False, default=datetime.now)
    NPL = models.FloatField(null=True, default=0, verbose_name='Non-Performing Loan - Nợ Xấu')
    LEV = models.FloatField(null=True, default=0, verbose_name='Leverage - Tỷ lệ nợ')
    class Meta:
        ordering = ['stock']
        unique_together = [['stock', 'year', 'provider']]

    def get_NPL(self):
        obj = debt.objects.get(
            stock=self.stock,
            provider = self.provider,
            year = self.year,
        )
        return obj.bad_debt / obj.total_debt
    
    def get_LEV(self):
        debt_ = debt.objects.get(
            stock=self.stock,
            provider=self.provider,
            year=self.year,
        )
        propertise_ = propertise.objects.get(
            stock=self.stock,
            provider=self.provider,
            year=self.year,
        )
        return debt_.total_debt / propertise_.total


"""
NPL (Non-Performing Loan - Nợ Xấu): Tỷ lệ nợ xấu của ngân hàng được tính bằng công thức: NPL = Nợ xấu / Tổng dư nợ cho vay * 100%

LLP (Loan loss provisioning - Tỉ lệ chi phí dự phòng rủi ro tín dụng): Tỉ lệ chi phí dự phòng rủi ro tín dụng được tính bằng công thức: LLP = Tổng số tiền dự phòng rủi ro tín dụng / Tổng dư nợ cho vay * 100%

LLR (Loan-loss reserve - Tỷ lệ dự phòng tổn thất cho vay): Tỷ lệ dự phòng tổn thất cho vay được tính bằng công thức: LLR = Tổng số tiền dự phòng tổn thất cho vay / Tổng dư nợ cho vay * 100%

LEV (Leverage - Tỷ lệ nợ): Tỷ lệ nợ được tính bằng công thức: Tổng nợ / Tổng tài sản * 100%.

ROE (Return On Equity - Lợi nhuận trên tổng số vốn chủ sở hữu): Lợi nhuận trên tổng số vốn chủ sở hữu được tính bằng công thức: ROE = Lợi nhuận sau thuế / Tổng số vốn chủ sở hữu * 100%.

ROA (Return on assets) = Lợi nhuận trên tổng tài sản doanh nghiệp = Lợi nhuận trước thuế / Tổng tài sản

EPS (Earnings per share) = Lợi nhuận trên cổ phiếu = Lợi nhuận sau thuế / Số cổ phiếu lưu hành
"""


class cryption(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    pub_key = models.TextField(null=False)
    pri_key = models.TextField(null=False)
    live_time = models.DateTimeField(null=False)


class stock_index(models.Model):
    stock = models.ForeignKey(stock, null=False, on_delete=models.CASCADE)
    provider = models.ForeignKey(provider, null=False, on_delete=models.CASCADE, default='FBC')
    ROE = models.FloatField(null=True, default=0, verbose_name='Return on Equity - Lợi nhuận trên tổng số vốn chủ sở hữu')
    ROA = models.FloatField(null=True, default=0, verbose_name='Return on assets - Lợi nhuận trên tổng tài sản doanh nghiệp')
    EPS = models.FloatField(null=True, default=0, verbose_name='Earnings per share - Lợi nhuận trên cổ phiếu')
    PA = models.FloatField(null=True, default=0, verbose_name='Price to Assets - Giá trị trên tài sản')
    PE = models.FloatField(null=True, default=0, verbose_name='Price to Earnings - Giá trị trên thu nhập')
