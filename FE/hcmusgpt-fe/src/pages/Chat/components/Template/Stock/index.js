import { Checkbox, Collapse, Tooltip } from 'antd';
import classNames from 'classnames/bind';
import { useEffect, useState } from 'react';
import 'tippy.js/dist/tippy.css';
import styles from './Stock.module.scss';

const cx = classNames.bind(styles);

const { Panel } = Collapse;

function Stock({ hook }) {
    const { stocks, stockChoice, setStockChoice } = hook;
    const [checkboxStock, setCheckboxStock] = useState([]);
    useEffect(() => {
        const data = stocks.map((item) => {
            return {
                label: item.name,
                value: item.id,
                alias: item.alias,
            };
        });
        setCheckboxStock(data);
    }, [stocks]);

    const onChangeHandler = (value) => {
        setStockChoice(value.map((item) => +item));
    };
    return (
        <div className={cx('wrapper')}>
            <Collapse>
                <Panel header="Ngân Hàng" key="2" className={cx('panel')}>
                    <div className={cx('list')}>
                        <Checkbox.Group
                            style={{
                                width: '100%',
                                display: 'flex',
                                flexWrap: 'wrap',
                                justifyContent: 'space-between',
                                alignItems: 'center',
                                alignContent: 'space-between',
                                padding: '10px',
                            }}
                            onChange={onChangeHandler}
                            defaultValue={stockChoice}
                        >
                            {checkboxStock.map((item) => {
                                return (
                                    <Tooltip title={item?.alias}>
                                        <Checkbox
                                            key={item.value}
                                            value={item.value}
                                            style={{
                                                width: '30%',
                                                margin: '0 0 10px 0',
                                                flex: '0 0 30%',
                                            }}
                                        >
                                            {item.label}
                                        </Checkbox>
                                    </Tooltip>
                                );
                            })}
                        </Checkbox.Group>
                    </div>
                </Panel>
            </Collapse>
        </div>
    );
}

export default Stock;
