/* eslint-disable jsx-a11y/alt-text */
/* eslint-disable react-hooks/exhaustive-deps */
import { faSignOut } from '@fortawesome/free-solid-svg-icons';
import { Layout, Modal } from 'antd';
import classNames from 'classnames/bind';
import { useEffect, useState } from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { AugmentedReality, CalendarIcon, Logo, ReadyStock } from '../../img';
import styles from './Chat.module.scss';

import { useLogin } from '../../pages/SignIn/hooks/login';
import { ChatContent, Guide, Template } from './components';
import { useChat } from './hooks';

const { Provider, Stock, Year } = Template;
const { Sider, Content } = Layout;

const cx = classNames.bind(styles);

function Chat() {
    const [collapsed, setCollapsed] = useState(false);
    const chatHook = useChat({});
    const loginHook = useLogin({});
    const { setError, open, setOpen } = loginHook;

    useEffect(() => {
        chatHook.fetchProviders();
        chatHook.fetchStocks();
    }, []);

    return (
        <>
            <Guide hook={chatHook} />
            <Layout className={cx('chat-container')}>
                <Sider
                    className={cx('side-bar')}
                    width={280}
                    collapsible
                    collapsed={collapsed}
                    onCollapse={(value) => setCollapsed(value)}
                >
                    <div className={cx('logo-container')}>
                        <img alt="logo" className={cx('logo')} src={Logo} />
                    </div>
                    <div className={cx('sider-collapse')}>
                        {collapsed ? (
                            <div className={cx('collapse-icon')} onClick={() => setCollapsed(false)}>
                                <img src={AugmentedReality} alt="provider" />
                            </div>
                        ) : (
                            <Provider hook={chatHook} />
                        )}
                        <br />
                        {collapsed ? (
                            <div className={cx('collapse-icon')} onClick={() => setCollapsed(false)}>
                                <img src={ReadyStock} alt="stock" />
                            </div>
                        ) : (
                            <Stock hook={chatHook} />
                        )}
                        <br />
                        {collapsed ? (
                            <div className={cx('collapse-icon')} onClick={() => setCollapsed(false)}>
                                <img src={CalendarIcon} alt="year" />
                            </div>
                        ) : (
                            <Year hook={chatHook} />
                        )}
                        <br />
                    </div>
                    <div onClick={() => setOpen(true)} className={cx('logout-button')}>
                        {collapsed ? (
                            <FontAwesomeIcon className={cx('icon-show')} icon={faSignOut} />
                        ) : (
                            <>
                                Đăng xuất
                                <FontAwesomeIcon className={cx('icon-logout')} icon={faSignOut} />
                            </>
                        )}
                    </div>
                </Sider>
                <Layout className={cx('site-layout')}>
                    <Content className={cx('site-layout-background')}>
                        <ChatContent hook={chatHook} />
                    </Content>
                </Layout>
            </Layout>

            <Modal
                className={cx('modal-warning')}
                open={open}
                onCancel={async () => {
                    await setOpen(false);
                    setError((prev) => false);
                }}
                footer={null}
            >
                <div className={cx('container-warning')}>
                    <h2 className={cx('title-warning')}>
                        Cuộc hội thoại sẽ bị xóa khi đăng xuất hoặc làm mới lại trang!!!!
                    </h2>
                    <img className={cx('img-warning')} src="https://cdn-icons-png.flaticon.com/512/4201/4201973.png" />
                    <div className={cx('container-button')}>
                        <button
                            onClick={async () => {
                                await chatHook.handleConfirmLogout();
                                setOpen(false);
                                setError((prev) => false);
                            }}
                            className={cx('button-warning')}
                        >
                            Xác Nhận
                        </button>
                        <button
                            onClick={async () => {
                                await setOpen(false);
                                setError((prev) => false);
                            }}
                            className={cx('button-warning')}
                        >
                            Hủy Bỏ
                        </button>
                    </div>
                </div>
            </Modal>
        </>
    );
}

export default Chat;
