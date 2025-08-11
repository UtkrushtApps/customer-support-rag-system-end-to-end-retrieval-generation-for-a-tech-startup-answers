import os
from typing import List, Dict

def load_corpus() -> List[Dict]:
    # Example: Simulate realistic support corpus
    return [
        {
            'doc_id': 'faq_1',
            'title': 'How to reset your device',
            'content': (
                'To reset your device, hold the power button for 10 seconds '
                'until the LED indicator flashes. This will perform a soft reset. '
                'If that does not work, consult the troubleshooting section.'
            ),
            'source': 'FAQ'
        },
        {
            'doc_id': 'manual_1',
            'title': 'Charging Instructions',
            'content': (
                'Use the supplied USB-C cable to charge your device. A full charge '
                'takes around 2 hours. If your device does not charge, try another cable or port.'
            ),
            'source': 'Manual'
        },
        {
            'doc_id': 'faq_2',
            'title': 'Connecting to Wi-Fi',
            'content': (
                'Go to Settings > Network > Wi-Fi, select your network, and enter your password. '
                'If you have trouble connecting, restart your router and device.'
            ),
            'source': 'FAQ'
        },
        {
            'doc_id': 'troubleshoot_1',
            'title': 'Device Not Turning On',
            'content': (
                'If your device does not turn on, charge it for at least 30 minutes. '
                'If it still does not power up, try a reset or contact support.'
            ),
            'source': 'Troubleshooting Guide'
        },
        {
            'doc_id': 'faq_3',
            'title': 'Factory Reset',
            'content': (
                'To perform a factory reset, navigate to Settings > System > Reset. '
                'Warning: This will erase all user data.'
            ),
            'source': 'FAQ'
        }
    ]
