import classNames from 'classnames/bind';

import { Collapse, Slider } from 'antd';
import styles from './Year.module.scss';

const cx = classNames.bind(styles);
const { Panel } = Collapse;
function Year({ hook }) {
    const { year, setYear } = hook;
    const marks = {
        2010: '2010',
        2022: '2022',
    };

    const onChange = (value) => {
        setYear({ min: value[0], max: value[1] });
    };
    return (
        <div className={cx('wrapper')}>
            <Collapse>
                <Panel header="Khoảng Năm" key="3" className={cx('panel')}>
                    <Slider
                        range
                        marks={marks}
                        defaultValue={[year.min, year.max]}
                        min={2010}
                        max={2022}
                        step={1}
                        onChange={onChange}
                    />
                </Panel>
            </Collapse>
        </div>
    );
}

export default Year;
