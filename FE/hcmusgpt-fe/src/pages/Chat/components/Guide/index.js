import { CloseOutlined } from '@ant-design/icons';
import { Layout } from 'antd';
import { Content, Header } from 'antd/es/layout/layout';
import classNames from 'classnames/bind';
import styles from './Guide.module.scss';
const cx = classNames.bind(styles);

export default function Guide({ hook }) {
    const { hideGuide, setHideGuide } = hook;
    return (
        hideGuide && (
            <div className={cx('guide')}>
                <Layout className={cx('guide-container')}>
                    <Header className={cx('guide-header')}>
                        <h1 style={{ margin: 0 }}>Hướng dẫn cho người dùng</h1>
                        <button className={cx('close-button')} onClick={() => setHideGuide(false)}>
                            <CloseOutlined />
                        </button>
                    </Header>
                    <Content>
                        <span>
                            <h2 className={cx('header')}>1. Chọn nhà cung cấp</h2>
                            <p className={cx('text-content')}>
                                Chọn nhà cung cấp bằng cách check vào những nhà cung cấp nào cần tìm ở thanh sidebar
                            </p>
                            <h2 className={cx('header')}>2. Chọn mã cổ phiếu</h2>
                            <p className={cx('text-content')}>
                                Chọn mã cổ phiếu bằng cách check vào mã cổ phiếu cần tìm ở thanh sidebar
                            </p>
                            <h2 className={cx('header')}>3. Chọn năm</h2>
                            <p className={cx('text-content')}>
                                Chọn năm bằng cách kéo thanh cho biết khoảng thời gian từ năm nào đến năm nào
                            </p>
                            <h2 className={cx('header')}>4. Nhập thông tin cần tìm</h2>
                            <p className={cx('text-content')}>Nhập thông tin cần tìm bằng cách nhập vào ô tìm kiếm</p>
                            <p className={cx('container-content')}>
                                {' '}
                                <b>(*)</b>: nếu thông tin cần nhập liên quan đến tiền xin hãy nhập đơn vị của tiền tệ
                                của bạn.
                            </p>
                            <h2 className={cx('header')}>5. Định nghĩa</h2>
                            <p className={cx('text-content')}>
                                <span className={cx('text-info')}>NPL (Non-Performing Loan - Nợ Xấu): </span>Tỷ lệ nợ
                                xấu của ngân hàng được tính bằng công thức: NPL = Nợ xấu / Tổng dư nợ cho vay * 100%
                            </p>
                            <p className={cx('text-content')}>
                                <span className={cx('text-info')}>
                                    LLP (Loan loss provisioning - Tỉ lệ chi phí dự phòng rủi ro tín dụng):{' '}
                                </span>
                                Tỉ lệ chi phí dự phòng rủi ro tín dụng được tính bằng công thức: LLP = Tổng số tiền dự
                                phòng rủi ro tín dụng / Tổng dư nợ cho vay * 100%
                            </p>
                            <p className={cx('text-content')}>
                                <span className={cx('text-info')}>
                                    LLR (Loan-loss reserve - Tỷ lệ dự phòng tổn thất cho vay):{' '}
                                </span>
                                Tỷ lệ dự phòng tổn thất cho vay được tính bằng công thức: LLR = Tổng số tiền dự phòng
                                tổn thất cho vay / Tổng dư nợ cho vay * 100%
                            </p>
                            <p className={cx('text-content')}>
                                <span className={cx('text-info')}>LEV (Leverage - Tỷ lệ nợ): </span>Tỷ lệ nợ được tính
                                bằng công thức: Tổng nợ / Tổng tài sản * 100%.
                            </p>
                            <p className={cx('text-content')}>
                                <span className={cx('text-info')}>
                                    ROE (Return On Equity - Lợi nhuận trên tổng số vốn chủ sở hữu):{' '}
                                </span>
                                Lợi nhuận trên tổng số vốn chủ sở hữu được tính bằng công thức: ROE = Lợi nhuận sau thuế
                                / Tổng số vốn chủ sở hữu * 100%.
                            </p>
                            <p className={cx('text-content')}>
                                <span className={cx('text-info')}>ROA (Return on assets) </span>= Lợi nhuận trên tổng
                                tài sản doanh nghiệp = Lợi nhuận trước thuế / Tổng tài sản
                            </p>
                            <p className={cx('text-content')}>
                                <span className={cx('text-info')}>EPS (Earnings per share) </span>= Lợi nhuận trên cổ
                                phiếu = Lợi nhuận sau thuế / Số cổ phiếu lưu hành
                            </p>
                            <h2 className={cx('header')} style={{ color: 'red' }}>
                                6. *Lưu ý
                            </h2>
                            <p className={cx('text-content')} style={{ color: 'red' }}>
                                Khi làm mới lại trang (nhấn phím F5) thì lịch sử đoạn hội thoại sẽ bị mất!!!
                            </p>
                        </span>
                    </Content>
                </Layout>
            </div>
        )
    );
}
