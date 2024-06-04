use pathfinding::prelude::absdiff;
use regex::Regex;
use std::collections::BTreeMap;

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Pos(i32, i32, i32);

impl Pos {
    fn distance(&self, other: &Pos) -> i32 {
        absdiff(self.0, other.0) + absdiff(self.1, other.1) + absdiff(self.2, other.2)
    }
}

#[aoc_generator(day23)]
fn input_generator(input: &str) -> Vec<(Pos, i32)> {
    let re = Regex::new(r"-?\d+").unwrap();
    input
        .lines()
        .map(|l| {
            let mut ns = re.captures_iter(l).map(|c| c[0].parse::<i32>().unwrap());
            (
                Pos(ns.next().unwrap(), ns.next().unwrap(), ns.next().unwrap()),
                ns.next().unwrap(),
            )
        })
        .collect()
}

#[aoc(day23, part1)]
fn part1(bots: &[(Pos, i32)]) -> usize {
    let (pos, radius) = bots.iter().max_by_key(|&(_, r)| r).unwrap();
    bots.iter()
        .filter(|&(p, _)| pos.distance(p) <= *radius)
        .count()
}

#[aoc(day23, part2)]
fn part2(bots: &[(Pos, i32)]) -> i32 {
    let mut dist = BTreeMap::new();
    for (pos, range) in bots {
        let d = pos.0 + pos.1 + pos.2;
        *dist.entry(d - range).or_insert(0) += 1;
        *dist.entry(d + range + 1).or_insert(0) -= 1;
    }
    let run = dist
        .iter()
        .scan(0i32, |s, (d, &x)| {
            *s += x;
            Some((d, *s))
        })
        .collect::<Vec<_>>();
    let max = run.iter().map(|&(_, n)| n).max().unwrap();
    let intervals = run
        .iter()
        .zip(run.iter().skip(1))
        .filter_map(
            |(&(a, n), &(b, _))| {
                if n == max {
                    Some((*a, *b - 1))
                } else {
                    None
                }
            },
        )
        .collect::<Vec<_>>();
    if intervals.iter().any(|&(a, b)| a <= 0 && b >= 0) {
        0
    } else {
        intervals
            .iter()
            .map(|&(a, b)| if b < 0 { -b } else { a })
            .min()
            .unwrap()
    }
}
