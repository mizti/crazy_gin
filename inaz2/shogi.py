#!/usr/bin/env python

class Shogi():
    # 0 = empty, 1 = friend, 2 = king
    board = [
        0, 0, 0, 0, 2, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 1, 0,
        0, 0, 1, 0, 0, 1, 0, 0, 0,
        0, 0, 1, 1, 0, 0, 0, 1, 0,
        1, 1, 0, 0, 0, 0, 1, 0, 1,
        0, 0, 0, 1, 0, 1, 0, 0, 0,
        1, 1, 1, 0, 1, 0, 1, 1, 1,
    ]
    moves = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    def step(self, xy, flags, depth):
        if depth >= 20:
            return [flags['got_king'] and not flags['is_fallen'] and not flags['killed_friend']]

        results = []
        for move in Shogi.moves:
            flags2 = dict(flags)
            xy2 = (xy[0] + move[0], xy[1] + move[1])
            is_now_fallen = not (0 <= xy2[0] <= 8 and 0 <= xy2[1] <= 8)
            flags2['is_fallen'] = flags2['is_fallen'] or is_now_fallen
            if not is_now_fallen:
                flags2['got_king'] = flags2['got_king'] or (Shogi.board[xy2[1]*9+xy2[0]] == 2)
                flags2['killed_friend'] = flags2['killed_friend'] or (Shogi.board[xy2[1]*9+xy2[0]] == 1)
            sub_results = self.step(xy2, flags2, depth+1)
            results.extend(sub_results)
        print xy, flags, depth
        return results

    def run(self):
        initial_flags = {'got_king': False, 'is_fallen': False, 'killed_friend': False}
        results = self.step((5, 5), initial_flags, 0)
        print float(sum(results))/len(results)

if __name__ == '__main__':
    Shogi().run()
