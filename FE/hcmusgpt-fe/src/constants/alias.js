export const ALIAS = {
    // Tài sản
    cash: 'Tiền mặt, vàng, bạc',
    deposit: 'Tiền gửi tại ngân hàng nhà nước',
    loan_credit_institutions: 'Cho vay các tổ chức tín dụng',
    loan_customer: 'Cho vay khách hàng',
    total: 'Tổng tài sản',

    // Nợ
    bad_debt: 'Nợ xấu',
    total_debt: 'Dư nợ (Tổng nợ)',

    // Thu nhập
    net_interest_income: 'Lãi thuần',
    interest_income: 'Lãi',
    service_activities: 'Lợi nhuận từ hoạt động dịch vụ',
    other_activities: 'Lợi nhuận từ hoạt động khác',
    profit_after_tax: 'Lợi nhuận sau thuế',

    // Chỉ số

    NPL: 'Non-Performing Loan - Nợ Xấu',
    LEV: 'Leverage - Tỷ lệ nợ',

    // NPL (Non-Performing Loan - Nợ Xấu): Tỷ lệ nợ xấu của ngân hàng được tính bằng công thức: NPL = Nợ xấu / Tổng dư nợ cho vay * 100%
    // LLP (Loan loss provisioning - Tỉ lệ chi phí dự phòng rủi ro tín dụng): Tỉ lệ chi phí dự phòng rủi ro tín dụng được tính bằng công thức: LLP = Tổng số tiền dự phòng rủi ro tín dụng / Tổng dư nợ cho vay * 100%
    // LLR (Loan-loss reserve - Tỷ lệ dự phòng tổn thất cho vay): Tỷ lệ dự phòng tổn thất cho vay được tính bằng công thức: LLR = Tổng số tiền dự phòng tổn thất cho vay / Tổng dư nợ cho vay * 100%
    // LEV (Leverage - Tỷ lệ nợ): Tỷ lệ nợ được tính bằng công thức: Tổng nợ / Tổng tài sản * 100%.
    // ROE (Return On Equity - Lợi nhuận trên tổng số vốn chủ sở hữu): Lợi nhuận trên tổng số vốn chủ sở hữu được tính bằng công thức: ROE = Lợi nhuận sau thuế / Tổng số vốn chủ sở hữu * 100%.
    // ROA (Return on assets) = Lợi nhuận trên tổng tài sản doanh nghiệp = Lợi nhuận trước thuế / Tổng tài sản
    // EPS (Earnings per share) = Lợi nhuận trên cổ phiếu = Lợi nhuận sau thuế / Số cổ phiếu lưu hành

    ROE: 'Return on Equity - Lợi nhuận trên tổng số vốn chủ sở hữu',
    ROA: 'Return on assets - Lợi nhuận trên tổng tài sản doanh nghiệp',
    EPS: 'Earnings per share - Lợi nhuận trên cổ phiếu',
    PA: 'Price to Assets - Giá trị trên tài sản',
    PE: 'Price to Earnings - Giá trị trên thu nhập',
};
