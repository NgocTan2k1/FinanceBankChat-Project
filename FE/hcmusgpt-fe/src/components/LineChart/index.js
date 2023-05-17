import {
    CategoryScale,
    Chart as ChartJS,
    Legend,
    LineElement,
    LinearScale,
    PointElement,
    Title,
    Tooltip,
} from 'chart.js';
import classNames from 'classnames/bind';
import { Line } from 'react-chartjs-2';
import random_rgba from '../../utils/color.js';

import styles from './LineChart.module.scss';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const cx = classNames.bind(styles);
export default function LineChart({ years, dataRaw, title }) {
    const options = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: title,
            },
        },
    };
    const labels = years;

    const data = {
        labels,
        datasets: dataRaw.map((item) => ({
            label: item.name,
            data: item.data,
            borderColor: random_rgba(),
            backgroundColor: random_rgba(),
        })),
    };
    return (
        <div className={cx('line-chart-container')}>
            <Line style={{ width: '100%' }} options={options} data={data} />
        </div>
    );
}
